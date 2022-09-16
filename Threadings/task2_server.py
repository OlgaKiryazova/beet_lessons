import threading
import socket
import _thread

SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
PORT = 8001
lock = threading.Lock()


def client_thread(conn):
    print(threading.current_thread())
    while True:
        data = conn.recv(1024)
        if not data:
            print('Bye')
            lock.release()
            break
        conn.send(data)
    conn.close()


def server_(SERVER, PORT):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER, PORT))
    print('Server binded to  port', PORT)
    server.listen(5)
    print('Server is listening')

    while True:
        conn, addr = server.accept()
        lock.acquire()
        print(f'Connected to: {addr[0]}:{addr[1]}')

        _thread.start_new_thread(client_thread, (conn, ))


def main():
    server_(SERVER, PORT)


if __name__ == '__main__':
    main()
