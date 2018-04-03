""" Return whether an object is an instance of a class or of a subclass thereof. """

# isinstance() 는 개체가 클래스 또는 하위클래스의 인스턴스인지 참, 거짓을 반환한다.
# 첫번째 인자로는 객체를, 두번째 인자로는 클래스를 넣어서 첫번째 인자가 두번째 인자의 인스턴스인지를 확인한다.
# 두번째 인자에 tuple 이 들어가면, 첫번째 인자가 tuple 의 요소중 하나의 인스턴스이면 True
# 두번째 인자가 classinfo 가 아니거나 tuple 이 아닐경우 TypeError 가 발생한다.


class Person(object):
    name = 'flouie'


f = Person()

# f 가 Person 의 인스턴스이므로 True
print(isinstance(f, Person))

# f 는 list 의 인스턴스가 아니므로 False
print(isinstance(f, list))

li_ = [1, 2, 3]
# li_ 는 리스트 이므로 True
print(isinstance(li_, (list, dict)))

a = 10
# 5 는 int 이므로 False
print(isinstance(a, (dict, float, str)))
