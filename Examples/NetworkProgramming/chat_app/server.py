import socket
import threading

# Server Configuration
PORT = 5050
SERVER_IP = '127.0.0.1'  # Use '0.0.0.0' to accept connections on all available IPs.
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
BUFF_SIZE = 1024

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, PORT))

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(BUFF_SIZE)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode(FORMAT))
            nicknames.remove(nickname)
            break

def start():
    server.listen()
    print(f"Server is listening on {SERVER_IP}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")

        client.send("NICK".encode(FORMAT))
        nickname = client.recv(BUFF_SIZE).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode(FORMAT))
        client.send("Connected to the server!".encode(FORMAT))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    start()
