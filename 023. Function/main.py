# 함수는 수학의 함수와 유사하게, 0개 이상의 input에 대해 1개 이상의 output을 제공한다
# 프로그래밍에서는 재사용성 높은 부분을 함수로 별도 정의하여 사용하곤 한다

# 동적 타이핑 언어기에 함수에도 별도로 타입을 명시하지 않아도 된다
# def [function]([arguments])
def print_hello():
    # 0개의 인자
    print('hello')
    # 반환을 별도로 명시하지 않으면 자동으로 None을 반환

def sum(a, b):
    # 2개의 필수 인자. 함수 호출 시 필수적으로 전달해야 함
    return a + b

print(sum(1, 2))
# Positional하게 전달(위치 인자)할 수도 있고
print(sum(b=3, a=2))
# 키워드 형태로 전달(키워드 인자)해줄 수 있다

def sum(a=0, b=0):
    # 기본값이 명시된 2개의 선택 인자. 함수 호출 시 인자를 선택적으로 전달할 수 있으며 전달되지 않으면 기본값으로 처리
    return a + b

print(sum(1, 2))
# 위치 인자처럼 순서대로 넘겨주거나
print(sum(b=3))
# 특정 인자만 전달

def sum(a, b) -> int:
    # 리턴 타입을 명시해줄 수 있음
    return a + b

def sum(*args):
    # 하나의 asterisk로 시작하는 가변 위치 인자
    # Tuple로 변환됨
    s = 0
    for n in args:
        s += n

    return s
print(sum(1, 2, 3, 4, 5))

def print_some_param(**kwargs):
    # 두개의 asterisk로 시작하는 가변 키워드 인자
    # Dictionary로 변환됨
    print(kwargs['some_param'])
print_some_param(some_param=123)

# 따라서 Python 함수의 인자는 기본적으로 아래의 4가지로 분류된다
# 1. 필수 인자
# 2. 선택 인자
# 3. 가변 위치 인자 튜플
# 4. 가변 키워드 인자 딕셔너리

# 함수의 인자를 정의할 때,
# (1) 선택 인자를 필수 인자 앞에 정의할 수 없고,
# (2) 가변 키워드 인자를 가변 위치 인자 앞에 정의할 수 없으며,
# (3) 가변 인자들을 필수 인자나 선택 인자 앞에 정의할 수 없다
# 따라서 1 -> 2 -> 3 -> 4 순으로 인자를 정의해야 한다