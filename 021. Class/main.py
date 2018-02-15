# 클래스는 객체지향 프로그래밍의 필수 요소 중 하나다
# 클래스는 객체를 찍어내기 위한 틀이라고 생각하면 될 것 같다
# 클래스를 인스턴스화하면 객체가 나온다


class Account:
    # 클래스 내부의 변수는 '클래스 변수'와 '인스턴스 변수'로 나뉜다
    
    num_of_account = 0
    # 클래스 변수

    # 생성자
    def __init__(self, id, pw):
        # 객체 자체를 가르키는 self 키워드가 있음. Java의 this와 거의 동일
        self.id = id
        self.pw = pw
        # 인스턴스 변수
        Account.num_of_account += 1
        # 클래스 변수의 접근

    # 소멸자
    # del로 인해 소멸할 객체는 이 메소드를 call하며 소멸함
    def __del__(self):
        Account.num_of_account -= 1

    def login(self, id, pw):
        # 클래스의 메소드는 객체 자신을 가르키는 self를 명시적으로 받아야 함
        # self는 객체에서 메소드를 call하면 자동으로 채워짐
        if self.id == id and self.pw == pw:
            return True
        else:
            return False

acc1 = Account('idid', 'pwpw')
acc2 = Account('city7310', 'PlanB')
# 객체 생성

print(Account.num_of_account)
# 클래스 변수 접근

print(acc1.login('idid', 'pwpw'))
print(acc2.login('hello', 'pw'))
del acc1
# 수동으로 소멸자를 불러내는 부분.(acc1.__del__()과 같음) 객체의 참조가 0이 되면 자동으로 call되기도 함

print(Account.num_of_account)
