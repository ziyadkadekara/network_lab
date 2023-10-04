import socket
import threading

# Dictionary to store client connections
clients = {}

# Server configuration
HOST = '127.0.0.1'
PORT = 54321

def handle_client(client_socket, client_address):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from {client_address}: {message}")
                # Extract recipient and message content
                recipient, content = message.split(": ", 1)
                send_message(client_address, recipient, content)
    except Exception as e:
        print(f"Connection to {client_address} closed: {e}")
        remove_client(client_address, client_socket)

def send_message(sender_address, recipient, message):
    if recipient in clients:
        recipient_socket = clients[recipient]
        sender_name = str(sender_address)
        recipient_name = str(recipient)
        full_message = f"From {sender_name}: {message}"
        try:
            recipient_socket.send(full_message.encode('utf-8'))
        except:
            remove_client(recipient, recipient_socket)

def remove_client(address, client_socket):
    if address in clients:
        print(f"Connection to {address} closed.")
        del clients[address]
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")
        clients[str(client_address)] = client_socket

        # Create a thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
