import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Waiting for a connection...")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)

# Receive data from the client
data = client_socket.recv(1024)
print("Received:", data.decode())

# Send a response back to the client
response = "Hello, client!"
client_socket.send(response.encode())

# Close the sockets
client_socket.close()
server_socket.close()
