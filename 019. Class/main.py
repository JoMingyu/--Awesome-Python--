# 클래스는 객체지향 프로그래밍의 필수 요소 중 하나다
# 클래스를 인스턴스화하면 객체가 나오고, 객체는 클래스의 인스턴스이다. 클래스-인스턴스-객체 3가지 요소의 상호작용에 대해 이해할 수 있어야 한다


class Account:
    # 클래스 내부의 변수는 '클래스 변수'와 '인스턴스 변수'로 나뉜다
    
    num_of_account = 0
    # 클래스 변수

    # 생성자
    def __init__(self, id, pw):
        # 일반적인 객체지향 프로그래밍 패러다임에서, Class level 함수는 '메소드'라고 부름

        # 파이썬의 메소드에는 객체 자체를 가르키는 self 키워드가 있음. Java의 this와 동일한 역할이며 파이썬의 메소드는 객체 자신을 가르키는 self를 명시적으로 받아야 함
        self.id = id
        self.pw = pw
        # 인스턴스 변수
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
# 클래스 변수 접근

print(acc1.login('idid', 'pwpw'))
print(acc2.login('hello', 'pw'))
# 객체.메소드() 형태로 호출 시 self에는 해당 객체가 자동으로 들어간다
# 그렇다는 건 아래와 같이 함수를 호출할 수도 있다는 것
print(Account.login(acc1, 'idid', 'pwpw'))
# Class level로 호출하며 객체를 명시적으로 전달

del acc1
# 수동으로 소멸자를 불러내는 부분.(acc1.__del__()과 같음) 객체의 참조가 0이 되면 GC에 의해 자동으로 call됨

print(Account.num_of_account)
