# https://docs.python.org/3/library/copy.html
import copy
# 파이썬의 assignment는 객체를 복사하지 않고 해당 객체들을 바인딩할 뿐이다
# 따라서 mutable한 컬렉션, 또는 mutable한 값들을 가지고 있는 컬렉션이라면 copy 모듈이 필요하다

_list = [1, 2, 3, [1, 2]]

# - 단순 객체 복제
copied_list = _list

del copied_list[0]
print(_list)
# _list의 0번째 요소도 함께 사라짐

# - 얕은 복사
copied_list = copy.copy(_list)

del copied_list[0]
print(_list)
# 요소는 변화하지 않음

copied_list[1][0] = 999
print(_list)
# 내부의 mutable 객체는 같이 변화함

# - 깊은 복사
deep_copied_list = copy.deepcopy(_list)

deep_copied_list[2][0] = -100
print(_list)
# 완전히 다른 객체
