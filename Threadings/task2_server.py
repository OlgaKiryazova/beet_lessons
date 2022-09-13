import threading
import socket


SERVER = socket.gethostbyname(socket.gethostname())
PORT = 8001
lock = threading.Lock()
print(SERVER)


def client_thread(connection):
    print(threading.current_thread())
    while True:
        data = connection.recv(1024)
        if not data:
            print('Bye')
            lock.release()
            break
        connection.send(data)
    connection.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((SERVER, PORT))
    print('Server binded to  port', PORT)
    server.listen(5)
    print(f'Server is listening on {SERVER}')

    while True:
        conn, addr = server.accept()
        lock.acquire()
        print(f'Connected to: {addr[0]}:{addr[1]}')
        newthread = client_thread(conn)
        newthread.start()

