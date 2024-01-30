import socket
import threading

# Client Configuration
PORT = 5050
SERVER_IP = '127.0.0.1'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
BUFF_SIZE = 1024

def receive():
    while True:
        try:
            message = client.recv(BUFF_SIZE).decode(FORMAT)
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        if message[len(nickname)+2:].startswith(DISCONNECT_MESSAGE):
            client.send(DISCONNECT_MESSAGE.encode(FORMAT))
            client.close()
            break
        client.send(message.encode(FORMAT))

if __name__ == "__main__":
    nickname = input("Choose your nickname: ")

    # Create a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()
