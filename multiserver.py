import socket
import threading

# Dictionary to map usernames to client sockets
clients = {}

# Function to handle incoming messages from a client
def handle_client(client_socket, username):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                print(f"Connection from {username} closed")
                del clients[username]
                break

            # Parse the message, which should be in the format: "TO: recipient_username MESSAGE: your_message"
            message = data.decode('utf-8')
            recipient, msg = parse_message(message)

            # Send the message to the recipient, if it exists
            if recipient in clients:
                recipient_socket = clients[recipient]
                recipient_socket.send(f"From {username}: {msg}".encode('utf-8'))
            else:
                client_socket.send(f"User '{recipient}' not found.".encode('utf-8'))
        except Exception as e:
            print(f"Error handling client {username}: {str(e)}")
            del clients[username]
            break

# Function to parse the message and extract the recipient and message
def parse_message(message):
    recipient = None
    msg = None

    # Split the message into parts
    parts = message.split(" ")
    for i in range(len(parts)):
        if parts[i] == "TO:" and i + 1 < len(parts):
            recipient = parts[i + 1]
        elif parts[i] == "MESSAGE:" and i + 1 < len(parts):
            msg = " ".join(parts[i + 1:])

    return recipient, msg

# Create a socket for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server host and port
server_host = '192.168.10.121'
server_port = 12346

# Bind the socket to the host and port
server.bind((server_host, server_port))

# Listen for incoming connections
server.listen(5)
print(f"Server listening on {server_host}:{server_port}")

# Main loop to accept incoming connections
while True:
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address}")
    
    # Prompt the client for their username
    client_socket.send("Enter your username: ".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8')

    # Store the client socket with their username
    clients[username] = client_socket
    
    # Create a thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
    client_thread.start()

