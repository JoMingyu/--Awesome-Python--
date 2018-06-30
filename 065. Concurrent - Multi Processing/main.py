# https://docs.python.org/3/library/multiprocessing.html
import multiprocessing
# https://github.com/python/cpython/tree/3.6/Lib/multiprocessing/
# 프로세스 기반의 동시성을 구현해 보자. 멀티 스레딩에서 가지고 있었던 GIL의 문제를 해결한다
import time


def f(q):
    pid = multiprocessing.current_process().pid
    proc_name = multiprocessing.current_process().name
    # PID와 Process Name

    q.put([pid, proc_name])


if __name__ == '__main__':
    q = multiprocessing.Queue()
    # 내부적으로 배타 제어를 하고 있는 큐
    # 프로세스 간 객체를 교환하기 위해 사용

    # 멀티 스레딩 코드에서 threading.Thread를 multiprocessing.Process로 바꾸기만 하면 됨
    proc1 = multiprocessing.Process(target=f, args=(q,), name='first')
    proc1.start()
    proc1.join()
    
    proc2 = multiprocessing.Process(target=f, args=(q,), name='second')
    proc2.start()
    proc2.join()

    print(q.get())
    # queue에 get을 하면 consume되어 사라짐(자료구조의 queue와 동일)

    proc3 = multiprocessing.Process(target=f, args=(q,), name='third')
    proc3.start()
    proc3.join()

    proc4 = multiprocessing.Process(target=f, args=(q,), name='fourth')
    proc4.start()
    proc4.join()

    print(q.empty())
    # 큐가 비어있는지를 검사

    # print(q.qsize())
    # Mac OSX에서는 sem_getvalue()이 깨져서 NotImplementedError가 발생함

    print(q.get())
    print(q.get())
    print(q.get())

    print(q.empty())
