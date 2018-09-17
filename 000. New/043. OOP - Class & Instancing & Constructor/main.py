# Python은 객체지향 프로그래밍 패러다임을 지원하고 있으므로, OOP를 문제 없이 구현할 수 있다


class Something:
    # class [ClassName]
    pass
    # pass statement만으로 이루어진, 틀만을 가지고 있는 클래스
    # Python의 모든 클래스는 암시적으로 'object' 클래스를 상속받음

instance = Something()
# [ClassName]()

NewSomething = Something
# 클래스도 일급 객체로서 변수에 assign 가능
instance = NewSomething()


class Account:
    # 객체가 생성될 때 호출되는 생성자
    def __init__(self, id, pw):
        # 파이썬의 메소드에는 객체 자체를 가르키는 self 키워드가 있음
        # Java의 this와 동일한 역할이며 파이썬의 메소드는 객체 자신을 가르키는 self를 명시적으로 받아야 함

        self.id = id
        self.pw = pw
        # 인스턴스 속성
        # Python에서 객체의 속성은 기본적으로 dynamic하므로, id와 pw라는 새로운 속성을 생성하며 값을 할당

        # 생성자 메소드인 __init__처럼 인터프리터에 의해 간접적으로 호출되는 메소드를 매직 메소드라고 부르며,
        # __[name]__ 형태(매직 메소드는 언더스코어 부분에서 설명함)

    def login(self, id, pw):
        # self는 객체에서 메소드를 call하면 자동으로 채워짐
        if self.id == id and self.pw == pw:
            return True
        else:
            return False

acc1 = Account('idid', 'pwpw')
acc2 = Account('city7310', 'PlanB')
# 객체 생성. new와 같은 키워드가 필요하지 않음

print(acc1.login('idid', 'pwpw')) # True
print(acc2.login('hello', 'pw')) # False
# 객체.메소드() 형태로 호출 시 self에는 해당 객체가 자동으로 들어간다
# 아래와 같이 Class level로 호출하며 객체를 명시적으로 전달할 수도 있다
print(Account.login(acc1, 'idid', 'pwpw')) # True
