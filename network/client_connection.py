import socket
import threading

class ClientConnection:
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print("Connected to server")

        # Start a thread to listen for messages from the server
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def receive(self):
        while True:
            data = self.client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received from server: {data}")

    def send(self, message):
        self.client_socket.send(message.encode())
        print(f"Sent to server: {message}")

    def disconnect(self):
        self.client_socket.close()
        print("Disconnected from server")

# Client side
if __name__ == "__main__":
    client = ClientConnection('localhost', 5000)
    client.connect()

    def client_input_thread():
        try:
            while True:
                message = input("Enter a message to send: ")
                if message.lower() == "exit":
                    break
                client.send(message)
        except KeyboardInterrupt:
            pass
        client.disconnect()

    input_thread = threading.Thread(target=client_input_thread)
    input_thread.start()
