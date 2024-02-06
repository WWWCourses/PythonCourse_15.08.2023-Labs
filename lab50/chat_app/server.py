import socket
import threading

BUF_SIZE = 64
PORT = 5050
SERVER_IP = '127.0.0.1'
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!EXIT"

# Shared dictionary to keep track of client connections. Any access to `clients` is a critical section
# and must be protected with `client_lock` to ensure thread safety.
clients = {}
client_lock = threading.Lock()

def login(conn):
    # Get client user name:
    name = conn.recv(BUF_SIZE).decode(FORMAT)
    if not name:
        return False

    # Add client to clients:
    with client_lock:
        clients[conn] = name

    # Send welcome message:
    conn.send(f'Welcome to the CHAT, {name}!'.encode(FORMAT))
    return True

def broadcast(message, exclude_conn=None):
    """Send message to all clients, except current (exclude_conn)"""
    with client_lock:
        for client in list(clients.keys()):
            if client != exclude_conn:
                try:
                    client.send(message.encode(FORMAT))
                except:
                    continue  # Handle possible socket sending issues gracefully

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    if not login(conn):
        return

    broadcast(f'>>>{clients[conn]} joined the chat<<<', conn)

    try:
        while True:
            # Receive a message:
            msg = conn.recv(BUF_SIZE).decode(FORMAT)
            if (not msg) or (msg.upper() == DISCONNECT_MESSAGE):
                break

            print(f"[{clients[conn]}]: {msg}")

            broadcast(f'{clients[conn]}: {msg}', conn)
    finally:
        # Cleanup:
        user_name = clients.get(conn)
        with client_lock:
            if conn in clients:
                del clients[conn]

        broadcast(f">>>{user_name} left the chat<<<")
        conn.send('Bye!'.encode(FORMAT))
        conn.close()
        print(f"[CONNECTION CLOSED] {addr} disconnected.")

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    finally:
        server.close()

if __name__ == "__main__":
    # Create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Reuse address
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the host
    server.bind(ADDR)

    print("[STARTING] server is starting...")
    start()