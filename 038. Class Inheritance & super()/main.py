# 객체지향 프로그래밍의 필수 요소 중 하나인 클래스 상속을 손쉽게 표현할 수 있으며
# Python은 다중 상속을 허용한다
class Animal:
    def __init__(self, name):
        self.name = name
        
    def run(self):
        print('{} is running'.format(self.name))

class Cat(Animal):
    # [ClassName]([ParentClassName])
    def __init__(self, name):
        super(Cat, self).__init__(name)
        # 상위 클래스의 메소드 호출
        # super(현재 클래스, self).method()
        
    def run(self):
        # 메소드 오버라이딩(재정의, 덮어쓰기)
        print('Cat {} is running'.format(self.name))
        
    def cry(self):
        # 새로운 기능 추가
        print('Cat {} is crying'.format(self.name))

class Rabbit(Animal):
    def __init__(self, name):
        super(Rabbit, self).__init__(name)

cat = Cat('catty')
rabbit = Rabbit('carrot')

cat.run()
# Cat catty is running
cat.cry()
# Cat catty is crying

rabbit.run()
# carrot is running(Animal 클래스에 정의된 메소드)