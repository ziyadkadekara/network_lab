import socket
import threading

# Client configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 54321

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection to the server closed.")
            client_socket.close()
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        recipient = input("Enter recipient (e.g., '127.0.0.1:12345'): ")
        message = input("Enter your message: ")
        if recipient and message:
            full_message = f"{recipient}: {message}"
            client_socket.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    main()
