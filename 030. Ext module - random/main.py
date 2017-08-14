import random
# 랜덤 모듈은 간단해 보이는데 별로 안간단하다
# 함수가 엄청 많다

print(random.random())
# 0부터 1 사이의 실수를 리턴한다

print(random.randrange(1, 7))
# n과 m-1 사이의 숫자를 리턴한다

# 파이썬의 랜덤 모듈은 리스트와 참 잘 어울린다
lst = ['a', 'b', 'c', 'd']

random.shuffle(lst)
# 섞어준다
print(lst)

print(random.choice(lst))
# 선택장애를 해결할 수 있다
