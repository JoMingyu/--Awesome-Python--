# 자바의 어노테이션과 비슷해 보이지만, 많이 다르다

# 먼저 JS를 한번쯤 해봤거나, 일급 객체 개념에 대해 공부해 보았다면 한번쯤 봤을 Closure를 살펴보자
def outer_function(msg):
    def inner_function():
        print(msg)
    
    return inner_function

hi = outer_function('Hi')
bye = outer_function('Bye')

hi()
bye()
# 외부 함수가 내부 함수를 리턴하고, 내부 함수는 외부 함수의 지역변수를 참조하는 형태

# 이제 데코레이터 함수를 선언해 보도록 하자
def decorator(original_function):
    def wrapper():
        print('Before {} function is called'.format(original_function.__name__))
        return original_function()
    
    return wrapper
# 1. 데코레이터 함수인 decorator와

def display():
    print('display function called')
# 2. 일반 함수인 display를 각각 정의

decorated_display = decorator(display)
# 3. display 함수를 인자로 decorator 함수를 실행한 리턴을 할당
# 4. 이 리턴 값은 wrapper 함수가 되지만, 아직 실행되지 않은 상태

decorated_display()
# 5. 리턴받은 wrapper 함수를 호출하며 origin_function인 display 함수가 호출되며 print 함수가 호출됨

# 이딴 복잡한 구조를 사용하는 데코레이터를 사용하는 이유는
# 이미 만들어져 있는 코드를 수정하지 않고도 wrapper 함수를 이용해 여러가지 기능을 추가할 수 있기 때문

# 일반적으로 위처럼 데코레이터 함수를 호출하는 구문은 잘 사용하지 않고, '@' 심볼을 이용한 간단한 구문을 사용함
@decorator
def display():
    print('display function called!')

display()

# 인수를 가진 함수를 데코레이팅해야 한다면, wrapper 함수에 인자를 추가하고 호출 시 사용하면 된다
def decorator(original_function):
    def wrapper(*args, **kwargs):
        print('Before {} function is called'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    
    return wrapper

@decorator
def display(some, args):
    print('display function called with {} and {}'.format(some, args))

display('da', 'ta')
