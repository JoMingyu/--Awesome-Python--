# 파이썬은 GIL 구조 때문에 멑티 스레딩을 돌려도 각 스레드가 time sharing하며 돌아간다
# 그래서 병렬적으로 코드를 돌려야 할 경우(특히 계산) 멀티 스레딩보단 멀티 프로세싱을 쓴다
import multiprocessing
import time


def f():
    pid = multiprocessing.current_process().pid
    proc_name = multiprocessing.current_process().name
    # PID와 Process Name
    while True:
        print('Here is {0}({1})'.format(pid, proc_name))
        time.sleep(1)


if __name__ == '__main__':
    # 멀티 스레딩 코드에서 threading.Thread를 multiprocessing.Process로 바꾸기만 하면 됨
    multiprocessing.Process(target=f, name='first').start()
    multiprocessing.Process(target=f, name='second').start()
    multiprocessing.Process(target=f, name='PlanB').start()
    multiprocessing.Process(target=f, name='NoName!').start()
