import socket
import threading

PORT = 5050
SERVER_IP = '127.0.0.1'
BUF_SIZE = 1024

# open TCP socket:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse address (optional, only for test purposes)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind( (SERVER_IP, PORT) )
server.listen()

print(f"Server is listening on {SERVER_IP}")

clients = []
def handle_client(conn):
    while True:
        msg = conn.recv(BUF_SIZE).decode()
        print(msg)

        # send msg to all clients, except current
        for client in clients:
            client.send(msg.encode())


while True:
    conn, addr = server.accept()
    print(f"Client Connectd: {addr}")

    clients.append(conn)

    # handle_client(conn)
    tr = threading.Thread(target=handle_client, args=(conn,))
    tr.start()




