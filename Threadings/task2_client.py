
import socket

SERVER = '192.168.0.101'
PORT = 8001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((SERVER, PORT))
    msg = 'Hello'
    while True:
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print('Received from the server:', str(data.decode('utf-8')))
        ans = input('\nDo you want to continue(y/n)?\n')
        if ans == 'y':
            continue
        else:
            break

