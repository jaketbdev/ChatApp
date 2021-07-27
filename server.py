import socket
import sys

stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port=8080
server_address = ((host, port))

print("Connecting")

stream_socket.connect(server_address)

message='message'
stream_socket.sendall(message)


data = stream_socket.recv(10)
print(data)

print('Socket Closed')
stream_socket.close()
