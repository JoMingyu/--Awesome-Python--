import random
# random 모듈엔 많은 함수가 있다


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
