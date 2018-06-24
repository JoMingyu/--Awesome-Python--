# https://docs.python.org/3/library/operator.html
from operator import *
# https://github.com/python/cpython/blob/3.6/Lib/operator.py
# 소스 코드를 보면 알 수 있듯, Python의 표준 연산자들의 함수 wrapper

print(lt(1, 2))
# True
# 1 < 2
print(le(2, 2))
# True
# 2 <= 2

print(ge(2, 1))
# True
# 2 > 1
print(gt(2, 2))
# True
# 2 >= 2

print(eq(3, 4))
# False
# 3 == 4
print(ne(3, 4))
# True
# 3 != 4

print(truth(1))
# True
# True if 1 else False
print(not_(False))
# True
# not False

print(is_(type(1), int))
# True
# type(1) is int
print(is_not(type(1), str))
# True
# type(1) is not str

print(add(1, 2))
# 3
# 1 + 2

print(sub(3, 1))
# 2
# 3 - 1

print(mul(2, 2))
# 4
# 2 * 2

# rshift, pow, truediv, xor, concat, contains 등 모든 기본 연산들을 함수 형태로 사용할 수 있다