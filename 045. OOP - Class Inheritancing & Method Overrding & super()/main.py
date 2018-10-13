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
        # 상위 클래스의 메소드(여기서는 생성자) 호출
        # super(현재 클래스, self).method()
        
    def run(self):
        # 메소드 오버라이딩
        print('Cat {} is running'.format(self.name))
        super(Cat, self).run()
        # print문을 수행한 후, 상위 클래스의 run 메소드 호출

    def cry(self):
        # 새로운 기능 추가
        print('Cat {} is crying'.format(self.name))

class Rabbit(Animal):
    def __init__(self, name):
        super(Rabbit, self).__init__(name)

cat = Cat('catty')
rabbit = Rabbit('carrot')

cat.run() # Cat catty is running & catty is running
cat.cry() # Cat catty is crying

rabbit.run() # carrot is running
# Rabbit 클래스에는 run 메소드가 없으므로, 상위 클래스인 Animal 클래스에 정의된 메소드가 호출됨
