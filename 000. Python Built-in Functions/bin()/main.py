""" Return the binary representation of an integer. """

# bin() 함수는 정수 인자를 받아서 "0b"로 시작하는 2진수 문자열로 변환한다.
# 인자는 하나인데 2진법으로 계산할 정수를 받는다.
# 만약 정수가 아니면 TypeError 를 발생시킨다.

# '1010'
print(bin(10))

# '11111111'
print(bin(255))

# bin()은 인자로 들어온 객체의 __index__() 매직 메서드를 호출한다.
# 그래서 int 가 아니어도 인자로 들어온 객체내에 __index__() 가 정의되어있으면 bin 함수가 TypeError 를 일으키지 않는다.


class Something(object):
    component1 = 1
    component2 = 2
    component3 = 3

    def __index__(self):
        return self.component1 + self.component2 + self.component3


print(bin(Something()))
