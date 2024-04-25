# server.py
import socket
import re

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print('Server started. Waiting for clients...')
    running = True

    while running:
        client_socket, addr = server_socket.accept()
        server_num = '42'

        msg = client_socket.recv(1024).decode()

        # Parsing for Name
        pattern = r'Client of (.+):'
        match = re.search(pattern, msg)
        if match:
            name = match.group(1)

        # Parsing for Number
        pattern = r':\s*(\d+)'
        match = re.search(pattern, msg)
        if match:
            client_num = match.group(1)
        
        # Sending data to Client
        print(f'{name} connected to Server of Ethan Iwama')
        combined = str(int(server_num) + int(client_num))
        print(f'Server: {server_num}; Client: {client_num}; Combined: {combined}')
        response = 'Server of Ethan Iwama: ' + server_num
        if int(client_num) < 1 or int(client_num) > 100:
            response += '\nServer closing...'
            client_socket.sendall(response.encode())
            client_socket.close()
            running = False
        else:
            client_socket.sendall(response.encode())
            client_socket.close()

    print('Server has been closed.')
    server_socket.close()

if __name__ == '__main__':
    main()