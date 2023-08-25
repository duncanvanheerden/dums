import socket

class ServerConnection():
    
    def __init__(self):
        pass

    def create_server(self, host, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        return server_socket

    def accept_client(self, server_socket):
        client_socket, client_address = server_socket.accept()
        return client_socket, client_address

    def receive_and_print_messages(self, client_socket):
        while True:
            message = client_socket.recv(1024).decode()  # Adjust buffer size as needed
            if not message:
                break
            print(f"Received message from client: {message}")


if __name__ == "__main__":
    server_connection = ServerConnection()
    server_socket = server_connection.create_server('localhost', 8000)
    print("Server is listening...")

    client_socket, client_address = server_connection.accept_client(server_socket)
    print(f"Connected to client: {client_address}")

    server_connection.receive_and_print_messages(client_socket)
