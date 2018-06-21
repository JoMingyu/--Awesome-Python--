# 빌트인 함수는 Python이 개발되는 과정에서 만들어진 함수들을 말한다
# Python 3.6.4 기준 빌트인 함수는 총 68개가 있으며, 그 중 자주 사용하는 몇가지만 살펴보자
print('Hello', end='\n')
# print(*message, end='\n')
# 콘솔 출력을 위한 함수. end는 맨 마지막 부분의 출력문을 의미, 기본값은 \n(개행)

print(type(3))
# <class 'int'>
# type(obj)
# obj의 타입을 확인하기 위해 사용

print(isinstance(3, int))
# True
# isinstance(obj, class-or-type-or-tuple)
# obj가 전달된 타입에 속하는지를 반환

print(sum(1, 3))
# 4
# sum(a, b)
# a + b를 반환

print(divmod(13, 4))
# (3, 1)
# divmod(x, y)
# x를 y로 floor div한 몫과 나머지를 반환

print(max(4, 9, 1, 3, 8), min(4, 9, 1, 3, 8))
# 9 1
# max(arg1, arg2, *args), min(arg1, arg2, *args)
# 전달된 2개 이상의 인자 중 최대값/최소값을 반환

l = [2, 3, 1, 4]
print(len(l))
# 4
# len(obj)
# 전달된 객체의 길이를 반환, 객체 내에 __len__ 메소드가 있어야 함

print(sorted(l))
# [1, 2, 3, 4]
# sorted(iterable, cmp=None, key=None, reverse=False)
# 전달된 iterable을 정렬하여 반환

print(reversed(l))
# <list_reverseiterator object at 0x1042b50b8>
print(list(reversed(l)))
# [4, 1, 3, 2]
# reversed(sequence)
# 전달된 sequence를 역방향으로 뒤집은 iterator를 반환