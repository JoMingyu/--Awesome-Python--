list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# 파이썬의 내장 함수인 zip()을 이용해 여러 iterable 객체들을 순회할 수 있다
for a, b in zip(list1, list2):
    print(a, b)

# 두 리스트의 길이가 다르다면
del list2[0]

for a, b in zip(list1, list2):
    print(a, b)

# 짧은 iterable 객체를 기준으로 for가 돌아간다. 이를 해결하기 위해 itertools의 zip_longest 함수를 사용한다
from itertools import zip_longest

for a, b in zip_longest(list1, list2):
    print(a, b)

# 짧은 iterable 객체의 남은 자리는 None으로 채워진다
