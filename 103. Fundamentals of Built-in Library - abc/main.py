# 파이썬의 추상 클래스/메소드 표현 방식은 불완전하다
class Parent:
    def a(self):
        raise NotImplementedError


class Child(Parent):
    pass


# 이렇게 되면 `Child`가 a를 오버라이드하지 않았음을 메소드 호출 시점에만 알아낼 수 있다
Child().a() # NotImplementedError

# 이러한 느슨한 추상 메소드 표현 방식을 개선해주는 것이 abc
# 이것저것 많지만 대표적인 ABCMeta, abstractmethod를 써 보자
from abc import ABCMeta, abstractmethod


class Parent(metaclass=ABCMeta):
    # ABCMeta는 abstract class를 정의하는 용도로 사용할 수 있는 metaclass
    # ABCMeta에 의해 메타클래싱된 클래스는, 인스턴스화되는 시점에
    # 아래처럼 abstractmethod 데코레이터로 데코레이팅된 메소드가 클래스에 존재하는 경우 에러를 발생시킨다
    @abstractmethod
    # 반대로 말하면, ABCMeta로 메타클래싱되지 않은 클래스에서는 abstractmethod 데코레이터가 큰 의미가 없다
    def a(self):
        pass


class ChildWithoutOverride(Parent):
    pass


class ChildWithOverride(Parent):
    def a(self):
        pass


ChildWithoutOverride() # TypeError: Can't instantiate abstract class ChildWithoutOverride with abstract methods a
ChildWithOverride() # 정상 작동
