
import socket


def client_(server, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server, port))
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


def main():
    port = 8001
    server = '192.168.0.101'
    client_(server, port)


if __name__ == '__main__':
    main()