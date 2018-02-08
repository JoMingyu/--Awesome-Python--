# 파이썬은 연산자 오버로딩을 지원한다
# 연산자 오버로딩된 클래스의 인스턴스들은 각각 더하고, 빼는 등등의 일을 할 수 있다
# 대표적으로 datetime 모듈의 클래스들에서 연산자 오버로딩이 잘 되어 있다.


class Test:
    # 연산자 오버로딩은 매직 메소드들을 구현하여 만들어낼 수 있다
    # add, sub, mul, truediv, floordiv, mod, pow부터 lshift, rshift, and, or, xor, abs, eq, lt, gt 등이 있다
    # https://docs.python.org/3/reference/datamodel.html
    def __init__(self, n):
        self.n = n

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


o1 = Test(3)
o2 = Test(3)

print(o1 + o2)
print(o1 - o2)
print(o1 * o2)
print(o1 == o2)
print(o1 / o2)
print(o1 // o2)
print(o1 <= o2)
print(o1 < o2)
