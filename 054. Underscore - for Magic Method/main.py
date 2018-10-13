# 사용자가 직접 호출할 수도 있지만, 대부분의 경우 Python 인터프리터에 의해 호출되는 메소드를 매직 메소드라고 부른다

print(len([1, 2, 3])) # 3
print([1, 2, 3].__len__()) # 3
# 빌트인 함수 len은 사실 전달된 객체의 __len__ 메소드를 호출한다

# 알기 쉽게, __len__ 메소드가 정의된 클래스의 인스턴스를 len 함수에 전달해 보자
class AlwaysReturnLength100:
    def __len__(self):
        return 100

print(len(AlwaysReturnLength100())) # 100

# 이러한 매직 메소드를 정의하기 위해서도 언더스코어를 사용한다
# 두 개의 언더스코어로 시작하고, 종료되는 메소드를 매직 메소드라고 부른다
# 많은 빌트인 함수나 연산자가 객체의 매직 메소드를 호출하고, 그 매핑들 중 일부는 다음과 같다
# 객체 생성 -> obj.__init__()
# print(obj) -> obj.__repr__()
# len(obj) -> obj.__len__()
# str(obj) -> obj.__str__()
# in -> obj.__contains__()

class Dummy:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return 'a is {}, b is {}'.format(self.a, self.b)
    
    def __str__(self):
        return str(self.a) + str(self.b)


d = Dummy(1, 3)

print(d) # 'a is 1, b is 3'
print(str(d)) # '13'
