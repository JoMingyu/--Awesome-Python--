# 객체 간에 부모-자식 관계가 성립하는 경우(동물 - 고양이, 강아지 등)
# 상속 구조로 클래스를 설계할 수 있다
# 동물을 예로 들었을 때 부모 클래스는 간단히 이렇게 할 수 있다


class Animal:
    def walk(self):
        # 상위 클래스는 공통적인 특성을 가지는 메소드 같은것들을 선언해 둔다
        print(self.__class__.__name__, 'is walking')
        # 클래스 이름 가져오고 싶어서 해봤는데 잘 된다


# 그리고 상속은
class Cat(Animal):
    pass


class Dog(Animal):
    pass


cat1 = Cat()
cat1.walk()
# 상위 클래스의 메소드를 호출할 수 있다
