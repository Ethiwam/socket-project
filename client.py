# client.py
import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print('Please input an integer: ')
    val = input()
    msg = 'Client of Ethan Iwama: ' + str(val)
    client_socket.sendall(msg.encode())

    response = client_socket.recv(1024).decode()
    print('Received from server:\n', response)

    client_socket.close()

if __name__ == '__main__':
    main()