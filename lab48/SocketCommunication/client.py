import socket

# open client socket:
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data to specific address:
user_input = input('Enter message: ')
msg = user_input.encode('utf-8')
client.sendto(msg,('127.0.0.1', 9999))