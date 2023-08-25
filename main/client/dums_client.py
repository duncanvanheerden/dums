import socket

class ClientConnection():
    
    def __init__(self):
        pass

    def create_client(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return client_socket

    def connect_to_server(self, client_socket, host, port):
        client_socket.connect((host, port))

    def send_message(self, client_socket, message):
        client_socket.send(message.encode())


if __name__ == "__main__":
    client_connection = ClientConnection()
    client_socket = client_connection.create_client()
    client_connection.connect_to_server(client_socket, 'localhost', 8000)

    while True:
        message = input("Enter a message to send to the server: ")
        client_connection.send_message(client_socket, message)
