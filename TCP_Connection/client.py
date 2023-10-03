import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Send data to the server
message = "Hello, server!"
client_socket.send(message.encode())

# Receive a response from the server
response = client_socket.recv(1024)
print("Server response:", response.decode())

# Close the socket
client_socket.close()
