# https://docs.python.org/3/library/threading.html
# 멀티 스레딩은 병행성(Concurrency)을 구현하기 위한 가장 간단한 방법
import threading
import time


def func(arg):
    while True:
        print(arg)
        time.sleep(1)

t1 = threading.Thread(target=func, args=('hihi',))
# 1. threading 모듈의 Thread 클래스를 이용하는 경우
# 넘겨줄 인자를 설정할 땐 튜플로 설정해 주어야 한다

t1.daemon = True
# 스레드의 데몬 여부를 설정할 수 있다
# 데몬 스레드는 메인 스레드가 종료되면 함께 종료되는 스레드를 말한다
t1.start()


class T(threading.Thread):
    # 2. Thread 클래스를 상속받아 구현하는 경우
    def run(self):
        # Thread start 시 이 run() 메소드가 실행된다
        while True:
            print('hello?')
            time.sleep(1)

t2 = T()
t2.setDaemon(True)
# setDaemon 메소드로도 데몬 설정이 가능하다
t2.start()

time.sleep(5)
# 데몬 스레드를 살려두기 위해
print('### End ###')

# 파이썬은 GIL 구조로 인해 멀티 스레딩을 구현하더라도 실제는 1개의 스레드에서 각 요소가 time sharing하는 정말 말도 안되는 형태로 이루어진다
# http://city7310.blog.me/221151692012
