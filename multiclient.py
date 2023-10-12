import socket
import threading

# Function to receive and display messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except Exception as e:
            print(f"Error receiving message: {str(e)}")
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input("Enter message (e.g., 'TO: recipient_username MESSAGE: your_message'): ")
        if message.lower() == "exit":
            client_socket.send("exit".encode('utf-8'))
            break
        else:
            client_socket.send(message.encode('utf-8'))

# Create a socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server host and port
server_host = '192.168.10.121'  # Change to the server's IP address or hostname
server_port = 12346

# Connect to the server
try:
    client.connect((server_host, server_port))
except Exception as e:
    print(f"Error connecting to the server: {str(e)}")
    exit()

# Prompt the user for their username
username = input("Enter your username: ")
client.send(username.encode('utf-8'))

# Create threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages, args=(client,))
send_thread = threading.Thread(target=send_messages, args=(client,))

# Start the threads
receive_thread.start()
send_thread.start()

# Wait for both threads to finish
receive_thread.join()
send_thread.join()

# Close the client socket
client.close()

