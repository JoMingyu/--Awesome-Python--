# 빌트인 함수 type()을 이용해 객체의 타입을 확인할 수 있다
n = 3
s = 'PlanB'
l = []
d = {}

print(type(n))
# <class 'int'>
print(type(s))
# <class 'str'>
print(type(l))
# <class 'list'>
print(type(d))
# <class 'dict'>

# Python의 각 기본 타입에 해당되는 int(), str() 등의 빌트인 함수들을 이용해 타입을 변환할 수 있다
print(int('1'))
# 1
print(int(1.0))
# 1

print(float('1.82'))
# 1.82

print(str(99))
# '99'

print(bool('False'))
# True
# 비어 있지 않은 문자열은 True로 평가되므로

t = 1, 2, 3, 3
print(list(t))
# [1, 2, 3, 3]
print(set(t))
# {1, 2, 3}

l = [1, 2, 3, 3]
print(tuple(l))
# (1, 2, 3, 3)
print(set(l))
# {1, 2, 3}

s = {1, 2, 3}
print(list(s))
# [1, 2, 3]
print(tuple(s))
# (1, 2, 3)

d = {1: 10, 2: 20}
print(list(d))
# [1, 2]
# Dictionary의 __iter__()는 dict.keys()를 반환하므로
print(tuple(d))
# (1, 2)
print(set(d))
# {1, 2}