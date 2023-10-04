import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 12345)

# Send data to the server
message = "Hello, server!"
client_socket.sendto(message.encode(), server_address)

# Receive a response from the server
response, server_address = client_socket.recvfrom(1024)
print("Server response:", response.decode())

# Close the socket
client_socket.close()
