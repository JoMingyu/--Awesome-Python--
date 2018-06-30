# https://docs.python.org/3/library/threading.html
import threading
# https://github.com/python/cpython/blob/3.6/Lib/threading.py
# 가장 일반적이고 간단한 형태의 동시성 프로그래밍인 멀티 스레딩
import time


def func(arg):
    print('{} started with arguments {}'.format(threading.current_thread(), arg))

    thread_local = threading.local()
    # 스레드 로컬 변수. 스레드가 stop될 때까지 thread level에서 유지됨
    thread_local.x = 1

    while True:
        print('Current thread : {}'.format(threading.current_thread()))
        time.sleep(1)

        if thread_local.x == 5:
            break

        thread_local.x += 1

t1 = threading.Thread(target=func, args=('hihi',), name='temp')
# 1. threading 모듈의 Thread 클래스를 이용해 function 단위로 스레딩할 경우
# Thread(group, target, name, args, kwargs, verbose)
# 넘겨줄 인자를 설정할 땐 튜플로 설정해 주어야 한다

t1.name = 'My thread 1'
# name 프로퍼티로 스레드에 이름을 정해줄 수 있다
# 레거시 getter/setter API로 getName(), setName()도 사용할 수 있다

t1.daemon = True
# 메인 스레드가 종료되면 함께 종료되는, 데몬 스레드 여부를 설정할 수 있다


class T(threading.Thread):
    # 2. Thread 클래스를 상속받아 구현하는 경우
    def run(self):
        # Thread start 시 이 run() 메소드가 실행된다
        print('{} started'.format(threading.current_thread()))

        thread_local = threading.local()
        thread_local.x = 1

        while True:
            print('Current thread : {}'.format(threading.current_thread()))
            time.sleep(1)

            if thread_local.x == 5:
                break

            thread_local.x += 1

t2 = T()
t2.name = 'My thread 2'
t2.setDaemon(True)
# 레거시 setter API인 setDaemon() 메소드로도 데몬 설정이 가능하다

print('Active count : {}'.format(threading.active_count()))
# 스레드가 몇 개 동작하고 있는지. 스레드 시작 전이므로 1

print('Main thread : {}'.format(threading.main_thread()))
# 스레드를 동작시키는 주체(메인 스레드)

print('### Start ###')

t1.start()
t2.start()
print('Active count : {}'.format(threading.active_count()))
# 스레드가 몇 개 동작하고 있는지. 스레드 2개를 추가로 시작했으므로 3

t1.join()
t2.join()
# t1과 t2가 종료되기까지 대기

# 파이썬의 multithreading은 멀티 스레드 프로그래밍에서 생기는 문제(경쟁 상태, 기아, 데드략 등)를 해결하기 위해
# Lock, RLock, Semaphore, Event, Timer, Barrier 등을 지원한다
# 그러나 Python의 스레드들은 GIL(Global Interpreter Lock) 개념 때문에 실제로는 싱글 스레드 기반에서 time sharing을 하며 동작한다
# reference counting이 객체에 접근할 때마다 lock을 걸고 풀어야 해서 오버헤드가 굉장히 큰 탓에, GIL이 아직까지 사라지지 않고 있다