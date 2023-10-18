import socket
import threading

class ServerConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_sockets = []

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()

        print(f"Server is listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            self.client_sockets.append(client_socket)
            print(f"Connected to {client_address}")
            
            # Handle client communication in a new thread
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received: {data}")

    def broadcast(self, message):
        for client_socket in self.client_sockets:
            try:
                client_socket.send(message.encode())
            except:
                pass

        print(f"Broadcasted: {message}")

    def stop(self):
        for client_socket in self.client_sockets:
            client_socket.close()

        if self.server_socket:
            self.server_socket.close()

# Server side
if __name__ == "__main__":
    server = ServerConnection('localhost', 5000)
    server.start()

    def server_input_thread():
        while True:
            message = input("Enter message to broadcast: ")
            server.broadcast(message)

    input_thread = threading.Thread(target=server_input_thread)
    input_thread.start()

