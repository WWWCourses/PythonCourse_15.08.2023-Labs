import socket

# open and bind server socket:
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('127.0.0.1', 9999))
print(f"server listen on ('127.0.0.1', 9999)")

while True:
    # receive data from a client:
    msg,address = server.recvfrom(1024)
    print(f"Received from {address}: {msg.decode('utf-8')}")

