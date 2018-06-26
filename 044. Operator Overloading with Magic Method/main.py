# 사용자 정의 객체는 기본적으로 연산 불가능하다
class CantOperation:
    pass

o1 = CantOperation()
o2 = CantOperation()

print(o1 + o2)
# TypeError: unsupported operand type(s) for +: 'CantOperation' and 'CantOperation'

# Python은 연산자 오버로딩을 지원하며, 이는 매직 메소드를 통해 구현 가능하다
class Number:
    def __init__(self, n):
        self.n = n
    
    # add, sub, mul, truediv, floordiv, mod, pow부터
    # lshift, rshift, and, or, xor, abs, eq, lt, gt 등이 있다
    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        return self.n / other.n

    def __floordiv__(self, other):
        return self.n // other.n

    def __eq__(self, other):
        return self.n == other.n

    def __le__(self, other):
        return self.n <= other.n

    def __lt__(self, other):
        return self.n < other.n

    def __ge__(self, other):
        return self.n >= other.n

    def __gt__(self, other):
        return self.n > other.n

o1 = Number(3)
o2 = Number(4)

print(o1 + o2)
print(o1 - o2)
print(o1 * o2)
print(o1 == o2)
print(o1 / o2)
print(o1 // o2)
print(o1 <= o2)
print(o1 < o2)
# 대표적으로 Python에서 날짜와 시간을 다루기 위한 datetime의 클래스들에서 연산자 오버로딩을 지원하여,
# 두 날짜나 두 시간을 비교하고 계산하는 등의 일을 쉽게 수행할 수 있다