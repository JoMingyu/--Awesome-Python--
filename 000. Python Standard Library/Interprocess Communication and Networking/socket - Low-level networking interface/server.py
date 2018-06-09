# https://docs.python.org/3/library/socket.html
from socket import socket, AF_INET, SOCK_STREAM
# https://github.com/python/cpython/blob/3.6/Lib/socket.py
# 네트워크 프로그래밍의 기초 중 하나인 소켓 프로그래밍
# 소켓은 양방향 데이터 전송 가능

# TCP는 1:1, Byte Stream 형식으로 데이터를 주고받으며 3way handshake 과정 존재
# UDP는 1:1/1:n/n:m, Datagram 형식으로 데이터를 주고받으며 3way handshake 과정 미존재
# TCP가 UDP보다 빠르지만 그렇게 큰 차이는 나지 않음
import threading

server_socket = socket(AF_INET, SOCK_STREAM)
# family, type 순. 기본값은 위와 같은 AF_INET, SOCK_STREAM

server_socket.bind(('', 30000))
print('Bind Successfully')
# 소켓을 해당 호스트와 포트에 바인딩

server_socket.listen(100)
print('Listening')
# Connection 대기를 위해 서버를 on

client_socket, addr = server_socket.accept()
print('Waiting for connection')
# Connection 대기

print('Got connection : {0}'.format(addr))


# 채팅 구현을 위해 sender와 getter 함수를 따로 둠
def msg_sender():
    while True:
        data = input('')
        client_socket.send(data.encode('utf-8'))


def msg_getter():
    while True:
        print('Data Received : {0}'.format(client_socket.recv(1024).decode('utf-8')))


threading.Thread(target=msg_sender).start()
threading.Thread(target=msg_getter).start()
