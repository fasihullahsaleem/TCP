# tcp_server.py
import socket

def start_server(host='192.168.13.173', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f'Server listening on {host}:{port}')
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {conn}")
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f'Received: {data.decode()}')
                conn.sendall(data)  # Echo back to the client

if __name__ == "__main__":
    start_server()

