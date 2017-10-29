# 코드를 병렬로 실행시켜 보자
import threading
import time


def func(arg):
    while True:
        print(arg)
        time.sleep(1)

t1 = threading.Thread(target=func, args=('hihi',))
# threading 모듈의 Thread 클래스를 이용하는 경우
# 넘겨줄 인자를 설정할 땐 튜플로 설정해 주어야 한다

t1.daemon = True
# 스레드의 데몬 여부를 설정할 수 있다
# 데몬 스레드는 메인 스레드가 종료되면 함께 종료되는 스레드를 말한다
t1.start()


class T(threading.Thread):
    # Thread 클래스를 상속받아 구현하는 경우
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
