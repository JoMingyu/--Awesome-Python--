# https://docs.python.org/3/library/itertools.html
from itertools import *
# APL, Haskell, SML의 구성 요소에서 영감을 받아 파이썬에 적합한 형태로 iterator building block들을 구현
# 반복에 특화된 파이썬 빌트인 함수의 확장처럼 느껴진다
# 이거 잘 알면 잘난척할 수 있음

# -- 무한 iterator
c = count(10, 3)
print(next(c))
# 10
print(next(c))
# 13
print(next(c))
# 16

# count(start [,step])
# start부터 step만큼 증가하는 iterator 반환. range()와 일부 유사

c = cycle('ABCD')
print(next(c))
# 'A'
print(next(c))
# 'B'
print(next(c))
# 'C'
print(next(c))
# 'A'
print(next(c))
# 'B'

# cycle(p)
# 전달한 iterable 객체를 복사하고, 순환하며 계속해서 반환

r = repeat(3, 3)
print(next(r))
# 3
print(next(r))
# 3
print(next(r))
# 3
print(next(r))
# StopItertaion

# repeat(elem [,n])
# elem을 n번 반복하는 iterator 반환. n이 별도로 지정되지 않으면 무한히 반환

# -- 길이가 정해진 iterator
c = compress('ABCDEF', [1, 0, 0, 0, 1, 1])
print(next(c))
# 'A'
print(next(c))
# 'E'
print(next(c))
# 'F'
print(next(c))
# StopIteration

# compress(data, selectors)
# d[0] if s[0], d[1] if s[1], ... 형태의 iterator 반환

d = dropwhile(lambda x: x<10, [1, 4, 15, 8, 11])
print(next(d))
# 1
print(next(d))
# 4
print(next(d))
# 8
print(next(d))
# StopIteration

# dropwhile(pred, seq)
# pred가 true인 데이터만을 iterator로 반환

f = filterfalse(lambda x: x%2, range(5))
print(next(f))
# 0
print(next(f))
# 2
print(next(f))
# 4
print(next(f))
# StopIteration

# filterfalse(pred, seq)
# pred가 false인 데이터만을 iterator로 반환

z = zip_longest([1, 2], [1, 2, 3, 4], [1, 2, 3])
print(next(z))
# (1 1 1)
print(next(z))
# (2 2 2)
print(next(z))
# (3 3 3)
print(next(z))
# (4 4 4)
print(next(z))
# StopIteration

# zip_longest(p, q, ...)
# 가장 긴 iterable을 기준으로 zipping