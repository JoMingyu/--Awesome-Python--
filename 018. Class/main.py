# 클래스는 객체지향 프로그래밍의 필수 요소 중 하나다
# OOP를 참 많이 하긴 했지만 사실 객체지향은 참 어렵다
# 클래스는 객체를 찍어내기 위한 틀이라고 생각하면 될 것 같다
# 클래스를 인스턴스화하면 객체가 나온다!


class Account:
    # 일단 클래스 변수와 인스턴스 변수로 나뉜다
    num_of_account = 0
    # 이건 클래스 변수

    # 생성자
    def __init__(self, id, pw):
        # 객체만이 가지는 필드를 가리키는 self 키워드가 있음. this와 비슷
        self.id = id
        self.pw = pw
        # 이건 인스턴스 변수
        Account.num_of_account += 1
        # 클래스 변수의 접근

    # 소멸자
    def __del__(self):
        Account.num_of_account -= 1

    def login(self, id, pw):
        if self.id == id and self.pw == pw:
            return True
        else:
            return False

acc1 = Account('idid', 'pwpw')
acc2 = Account('city7310', 'PlanB')
# 객체 생성, new 키워드를 사용하지 않음
print(Account.num_of_account)
# 클래스 변수 접근
# 파이썬은 private 필드가 언어 차원에서 존재하지 않는 것 같음

print(acc1.login('idid', 'pwpw'))
print(acc2.login('hello', 'pw'))
acc1.__del__()
print(Account.num_of_account)
