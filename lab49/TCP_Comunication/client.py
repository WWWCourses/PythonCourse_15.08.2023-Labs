from pydoc import cli
import socket
import threading

PORT = 5050
SERVER_IP = '127.0.0.1'
BUF_SIZE = 1024

# open TCP socket:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect( (SERVER_IP, PORT) )
print(f'Client is connected to [{SERVER_IP, PORT}]')

def receive_message(client):
    answer = client.recv(BUF_SIZE)
    print(f'answer:{answer.decode()}')

while True:
    msg = input('>>>')
    client.send( msg.encode() )

    tr = threading.Thread(target=receive_message, args=(client, ))
    tr.start()


