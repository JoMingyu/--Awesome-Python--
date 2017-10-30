# 객체의 복사는 단순 객체복제, 얕은 복사(shallow copy), 깊은 복사(deep copy)로 나뉜다
l1 = [1, 2, 3]
l2 = l1
# 변수만 복사하고 있으니, 바라보는 객체는 당연히 동일할 것이다
print(l1 == l2)
# True
print(l1 is l2)
# True

# 즉, 두 개의 변수 중 하나만 변경되어도 나머지 하나도 동일하게 수정되는 현상이 발생한다
# l2를 변경시켜 보자
del l2[2]
# l2는 [1, 2]로 바뀌었을 것이다. 그런데 l1을 출력해 보면 함께 바뀌어 있다
print(l1)

# 기본적으로 mutable 객체일 때만 이와 같은 얕은 복사 문제가 생긴다
# 숫자나 문자열과 같은 immutable 객체는 위의 경우에 해당되지 않는다
a = 10
b = a
b = 20
print(a, b)
# b는 20으로 바뀌었으나 a는 그대로다

# 얕은 복사의 경우는, 객체는 별도로 생성하고 안에 들어가 있는 값은 같은 객체를 참조한다
l1 = [1, [1, 2, 3]]
l2 = list(l1)
# shallow copy
print(l1 == l2)
# True
print(l1 is l2)
# False

l2[0] = 100
l2[1][0] = 99
print(l1, l2)
# [1, [99, 2, 3]] [100, [99, 2, 3]]
# shallow copy가 발생해 만들어진 객체는 별도의 객체이므로 immutable item 수정은 복사본만 적용됨
# 하지만 copy된 내부의 item은 같은 객체를 바라보므로, 원래 들어가 있던 리스트는 mutable 하기 때문에 함께 수정됨

# copy 모듈의 deepcopy() 함수를 통해 깊은 복사를 손쉽게 구현할 수 있다
from copy import deepcopy

l2 = deepcopy(l1)
l2.append(9999)
print(l1)
# deep copy로 l3를 만들었기 때문에 l3를 조작하더라도 l1에는 영향을 끼치지 않는다
