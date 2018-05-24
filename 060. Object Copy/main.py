# 파이썬의 = 기호(assignment expression)는 객체를 복사하지 않고, 해당 객체의 주소를 바인딩할 뿐이다
# 따라서 mutable한 컬렉션, 또는 mutable한 값들을 가지고 있는 컬렉션이라면 copy 모듈이 필요하다
l = [1, 2, 3, [1, 2]]

# - 단순 객체 복제
copied_list = l
print(copied_list is l)
# True
# 객체를 단순히 대입하는 것이므로 서로 바라보는 주소가 동일

del copied_list[0]
print(l)
# [2, 3, [1, 2]]
# 원본 객체 l의 0번째 요소도 함께 사라짐

import copy

# -- 얕은 복사
# 복합객체는 별도로 생성하고, 그 안에 들어가는 내용은 원래와 같은 객체로 둠
copied_list = copy.copy(l)
print(copied_list is l)
# False
# 복합객체가 별도로 생성되었으므로 서로 주소가 다름

del copied_list[0]
print(copied_list, l)
# [3, [1, 2]] [2, 3, [1, 2]]
# 복사된 list에서 0번째 인덱스를 제거했으나, 원본 객체의 요소는 변화하지 않음

print(copied_list[1] is l[2])
# True
# 내부의 객체는 별도로 복사하지 않고 주소 참조만 시키므로 서로 주소가 같음
copied_list[1][0] = 999
print(l)
# [2, 3, [999, 2]]
# 따라서 내부의 mutable 객체는 함께 변화함

# -- 깊은 복사
# 복합객체를 새롭게 생성하며, 그 안의 내용까지 재귀적으로 새롭게 생성
deep_copied_list = copy.deepcopy(l)
print(deep_copied_list is l)
# False
print(deep_copied_list[2] is [2])
# False
# 완전히 새로운 객체

deep_copied_list[2] = -100
print(deep_copied_list, l)
# [2, 3, -100] [2, 3, [999, 2]]
# 원본 객체에 영향을 끼치지 않음
