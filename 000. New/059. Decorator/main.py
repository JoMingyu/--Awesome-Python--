# 외부 함수가 내부 함수를 반환하고, 해당 내부 함수는 외부 함수의 지역변수를 참조하는 closure

def outer(msg):
    def inner():
        print(msg)
    
    return inner

print_hi = outer('hi')
print_hi()

# 데코레이터는 함수 형태로 동작한다
def decorator(func):
    def wrapper():
        print('Function will be called')

        return func()
    
    return wrapper
    # decorator 함수에 전달된 func를 실행하여 그 결과를 반환하는 wrapper 함수 반환

def print_something():
    print('Hello!')

decorated_print_something = decorator(print_something)
# decorator 함수에 func라는 인자로 print_something 함수를 전달하고, 해당 decorator 함수가 반환하는 wrapper 함수를 받음

decorated_print_something()
# wrapper 함수를 호출하며, 이는 'Function will be called'를 출력하고 인자로 넘겨준 원본 함수(func)를 실행하여 그 결과를 반환

# 이런 복잡한 구조를 사용하는 데코레이터를 쓰는 이유는
# 이미 만들어져 있는 코드를 수정하지 않고도 여러가지 기능을 추가할 수 있기 때문
# 일반적으로 위처럼 데코레이터 함수를 호출하여 새로운 함수를 반환받는 구문은 잘 사용하지 않고, '@' 심볼을 사용

@decorator
def print_something():
    print('Hello!')

print_something()

# 인자를 가진 함수를 데코레이팅해야 한다면, wrapper 함수에 인자를 추가하고 원 함수를 호출할 때 인자를 전달하면 된다
def decorator(func):
    def wrapper(*args, **kwargs):
        print('Function will be called')

        return func(*args, **kwargs)
    
    return wrapper

@decorator
def print_msg(msg):
    print(msg)

print_msg('Hello?')

# 데코레이터 자체가 인자를 가져야 한다면, 인자를 받고, 데코레이터를 반환하는 함수로 데코레이터를 감싸주자
def decorator_having_argument(*args):
    def real_decorator(func):
        def wrapper():
            print('Function will be called')
            print('Decorator Arguments : {}'.format(args))

            return func()
        return wrapper
    return real_decorator
    # 내부의 실제 데코레이터 함수를 반환

@decorator_having_argument(1, 2, 3)
# decorator_having_argument 함수를 인자와 함께 호출하며, 해당 함수가 반환하는 내부의 실제 데코레이터 함수로 데코레이팅
def print_something():
    print('Hello!')

print_something()

# 전달할 인자가 없더라도, 함수를 호출하는 형태를 사용해야 한다(내부의 실제 데코레이터로 함수를 데코레이팅해야 하기 때문)
@decorator_having_argument()
def print_something():
    print('Hello!')

print_something()
