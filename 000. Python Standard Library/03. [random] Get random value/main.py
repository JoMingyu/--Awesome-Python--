# https://docs.python.org/3/library/random.html
import random
# 수많은 종류의 랜덤 값들을 다루기 위한 모듈
# 많은 함수들이 제공된다


print(random.random())
# 0부터 1 사이 실수 리턴

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
