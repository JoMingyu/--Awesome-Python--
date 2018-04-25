# 클라이언트 모듈
from socket import socket
import threading

client_socket = socket()
# == socket(AF_INET, SOCK_STREAM)

host = 'localhost'
port = 30000

client_socket.connect((host, port))
print('Connected {0}'.format(host))
# 해당 호스트와 포트에 connect


def msg_sender():
    while True:
        data = input('')
        client_socket.send(data.encode('utf-8'))
        # send에 들어가는 데이터는 bytes여야 함


def msg_getter():
    while True:
        print('Data Received : {0}'.format(client_socket.recv(1024).decode('utf-8')))
        # recv의 리턴 데이터는 bytes


threading.Thread(target=msg_sender).start()
threading.Thread(target=msg_getter).start()
