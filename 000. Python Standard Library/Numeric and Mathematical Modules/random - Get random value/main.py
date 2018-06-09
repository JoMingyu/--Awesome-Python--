# https://docs.python.org/3/library/random.html
import random
# https://github.com/python/cpython/blob/3.6/Lib/random.py
# 수많은 종류의 랜덤 값들을 다루기 위한 모듈
# 많은 함수들이 제공된다

random.seed()
# 랜덤 숫자 생성기를 초기화. 인자 'a'를 전달하지 않았거나 None이라면 현재 시스템의 시간이 시드 값으로 사용됨


print(random.random())
# 0부터 1 사이 실수 리턴

print(random.uniform(2, 10))
# 순서대로 전달한 a 이상 b 미만의 실수 리턴(a <= N < b)

print(random.triangular(0, 0.003))
# 순서대로 전달한 low, high 사이의 실수 리턴(low <= N <= high)

print(random.randint(1, 7))
# n과 m 사이 정수 리턴
print(random.randrange(1, 7))
# n과 m-1 사이 정수 리턴

# 파이썬의 랜덤 모듈은 iterable data들을 다룰 수 있다
lst = ['a', 'b', 'c', 'd']

random.shuffle(lst)
# list shuffle
print(lst)

print(random.choice(lst))
# 선택장애를 해결할 수 있다
