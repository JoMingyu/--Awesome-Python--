# 코드를 병렬로 실행시켜 보자
import threading
import time


def func(arg):
    while True:
        print(arg)
        time.sleep(1)

threading.Thread(target=func, args=('hihi',)).start()
