# Python은 객체지향 프로그래밍 패러다임을 지원하고 있으므로, OOP를 문제 없이 구현할 수 있다
# 클래스를 인스턴스화하면 객체가 나오고, 객체는 클래스의 인스턴스이다. 클래스-인스턴스-객체 3가지 요소의 상호작용에 대해 이해할 수 있어야 한다


class Something:
    pass
    # pass statement만으로 이루어진, 틀만을 가지고 있는 클래스


some = Something()
# [ClassName]()


class Account:
    num_of_account = 0
    # 모든 객체가 공유하는 클래스 필드

    # 객체가 생성될 때 호출되는 생성자
    def __init__(self, id, pw):
        # 파이썬의 메소드에는 객체 자체를 가르키는 self 키워드가 있음
        # Java의 this와 동일한 역할이며 파이썬의 메소드는 객체 자신을 가르키는 self를 명시적으로 받아야 함
        self.id = id
        self.pw = pw
        # 객체마다 가지는 인스턴스 필드
        Account.num_of_account += 1
        # 클래스 변수의 접근

    # 소멸자
    # del로 인해 소멸할 객체는 이 메소드를 호출함
    def __del__(self):
        Account.num_of_account -= 1

    def login(self, id, pw):
        # self는 객체에서 메소드를 call하면 자동으로 채워짐
        if self.id == id and self.pw == pw:
            return True
        else:
            return False

acc1 = Account('idid', 'pwpw')
acc2 = Account('city7310', 'PlanB')
# 객체 생성

print(Account.num_of_account)
# 클래스 필드 접근

print(acc1.login('idid', 'pwpw'))
print(acc2.login('hello', 'pw'))
# 객체.메소드() 형태로 호출 시 self에는 해당 객체가 자동으로 들어간다
# 아래와 같이 Class level로 호출하며 객체를 명시적으로 전달할 수도 있다
print(Account.login(acc1, 'idid', 'pwpw'))

del acc1
# 수동으로 소멸자를 호출

print(Account.num_of_account)
