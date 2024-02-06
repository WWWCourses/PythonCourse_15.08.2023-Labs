import socket
import threading
import sys

SERVER_IP = '127.0.0.1'  # Adjust as necessary
PORT = 5050
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!EXIT"
BUF_SIZE = 64

# Shared flag to indicate disconnection intent
is_disconnecting = False

def clear_line():
    """
    Clear the current line in the terminal.
    """
    sys.stdout.write('\r\033[K')
    sys.stdout.flush()

def receive_messages(client):
    global is_disconnecting
    try:
        while True:
            if is_disconnecting:
                break
            msg = client.recv(BUF_SIZE).decode(FORMAT)
            if msg:
                clear_line()
                print(f"{msg}\nyou: ", end='')
                sys.stdout.flush()
    except Exception as e:
        if not is_disconnecting:  # Only show the error if disconnection wasn't intended
            clear_line()
            print(f"Lost connection to server: {e}")
    finally:
        sys.exit()  # Ensure the program exits if this thread encounters an unexpected error

def send_messages(client):
    global is_disconnecting
    try:
        while True:
            msg = input("you: ")
            if msg.upper() == DISCONNECT_MESSAGE:
                is_disconnecting = True
                client.send(DISCONNECT_MESSAGE.encode(FORMAT))
                break
            else:
                client.send(msg.encode(FORMAT))
    finally:
        client.close()

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    name = input("Enter your name: ")
    client.send(name.encode(FORMAT))

    welcome_message = client.recv(BUF_SIZE).decode(FORMAT)
    print(welcome_message)

    thread_recv = threading.Thread(target=receive_messages, args=(client,))
    thread_send = threading.Thread(target=send_messages, args=(client,))

    thread_recv.daemon = True  # Allow program to exit even if this thread is running
    thread_recv.start()
    thread_send.start()
    thread_send.join()  # Wait for the send thread to finish

    print("\nDisconnecting from server.")
    client.close()