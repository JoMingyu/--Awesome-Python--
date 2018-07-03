"""Return the identity of an object."""
# 객체의 "ID"를 반환한다. 이 "ID" 는 개체 수명 동안 이 객체에 대해 고유하고 상수로 보장되는 정수이다.
# 겹치지 않는 수명을 가진 두개의 객체는 동일한 ID 값을 가질 수 있다. (반대로 수명이 겹치는 두 객체는 동일한 ID 값을 가질 수 없다.)
# python 공식 문서의 CPython 구현 세부 정보에 따르면, ID 값은 메모리에 있는 객체의 주소이다.


class Ex:
    num = 100


# 클래스의 주소(id)
print(id(Ex))

# 인스턴스의 주소(id)
ex = Ex()
print(id(ex))

# python 에서는 모든 것이 객체이므로 정수 1도 id 값을 가진다.
print(id(1))

# 변수 a 와 b 가 같은 1을 가리키므로 1, a, b 의 id 값은 같다
a = 1
b = a
print(id(1))
print(id(a))
print(id(b))
