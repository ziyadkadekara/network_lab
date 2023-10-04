import socket

# Create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Chat loop
while True:
    # Send a message to the server
    message = input("You: ")
    client_socket.send(message.encode())

    # Receive a response from the server
    response = client_socket.recv(1024)
    print(f"Server: {response.decode()}")

# Close the socket
client_socket.close()
