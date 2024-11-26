# tcp_client.py
import socket

def start_client(host='192.168.116.136', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = "Hello, Server!"
        client_socket.sendall(message.encode())
        
        data = client_socket.recv(1024)
        print(f'Received from server: {data.decode()}')

if __name__ == "__main__":
    start_client()
