# 함수는 수학의 함수와 유사하게, 0개 이상의 input에 대해 1개 이상의 output을 제공한다
# 프로그래밍에서는 재사용성 높은 부분을 함수로 별도 정의하여 사용하곤 한다
# 잘 쪼개진 함수 기반의 추상화 높은 코드를 작성하는 것은 정말 중요하다

def print_hello():
    # def [function_name]((arguments...))
    # 타입 추론이 되는 언어기에 함수에도 별도로 리턴 타입을 명시하지 않아도 된다
    print('hello')
    # 별도의 반환문이 없으면, 함수가 자동으로 None을 반환('return None'으로 처리)

def sum(a, b):
    # 2개의 필수 인자. 함수 호출 시 필수적으로 전달해야 함
    return a + b

print(sum(1, 2)) # 3
# Positional하게 전달
print(sum(b=3, a=2)) # 5
# 키워드 형태로 전달
# 각각을 위치 인자와 키워드 인자라고 부른다

def sum(a=0, b=0):
    # 기본값이 명시된 2개의 선택 인자. 함수 호출 시 인자를 선택적으로 전달할 수 있으며 전달되지 않으면 기본값으로 처리
    return a + b

print(sum(1, 2)) # 3
# 순서대로 모든 인자 전달
print(sum(1)) # 0
# 일부만 전달. 이 경우 b는 기본값인 0
print(sum(b=3)) # 3
# 특정 인자만 전달. 이 경우 a는 기본값은 0

def sum(*args):
    # 하나의 asterisk로 시작하는 가변 위치 인자
    # *[name]
    # 전달된 인자들은 'args'에 튜플로 관리됨
    s = 0
    for n in args:
        s += n

    return s

print(sum(1, 2, 3, 4, 5)) # 15

def print_some_param(**kwargs):
    # 두개의 asterisk로 시작하는 가변 키워드 인자
    # **[name]
    # 전달된 인자들은 'kwargs'에 '인자 이름: 값' 형태로 이루어진 Dictionary로 관리됨
    print(kwargs['some_param'])

print_some_param(some_param=123) # 123

# 따라서 Python에서 함수의 인자 형태는 기본적으로 아래의 4가지로 분류된다
# 1. 필수 인자
# 2. 선택 인자
# 3. 가변 위치 인자
# 4. 가변 키워드 인자

# 그리고 호출자 입장에서 함수의 인자 전달은 아래의 2가지 방법을 사용할 수 있다
# 1. 위치 인자
# 2. 키워드 인자

# 함수의 인자를 정의할 때,
# (1) 선택 인자를 필수 인자 앞에 정의할 수 없고,
# (2) 가변 키워드 인자를 가변 위치 인자 앞에 정의할 수 없으며,
# (3) 가변 인자들을 필수 인자나 선택 인자 앞에 정의할 수 없다
# 따라서 필수 -> 선택 -> 가변 위치 -> 가변 키워드 순으로 인자를 정의해야 한다
def f(a, b, c=0, d=0, *args, **kwargs):
    pass

f(1, 2, d=3, other=15)
# a에 1, b에 2, d에 3, kwargs에 {'other': 15}가 바인딩되고
# c는 기본값은 0, args는 전달된 별도의 위치 인자가 없으므로 []
