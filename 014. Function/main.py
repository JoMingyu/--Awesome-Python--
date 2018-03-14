# 함수를 통해 코드를 좀 짜임새 있게 짤 수 있다
# print라는 것도 하나의 함수다
print('hello world')
# 얘네는 builtin function(언어 설계 과정에서 만들어져 기본적으로 지원되는 함수들)이라고 부른다
# 사용자 정의 함수를 선언하는 방법을 알아야 한다
# 파이썬의 함수는 오버로딩 불가능하므로, 기본값 처리된 인자를 활용하여 오버로딩을 흉내낼 수 있다


def print_hello():
    # 함수 선언은 def
    # 함수 이름은 PEP8 표준에 따라 snake case
    print('Hello')
    # 함수의 리턴은 있을 수도 있고 없을 수도 있다

print_hello()

# 파이썬의 함수는 일급 객체이므로, 변수에 할당할 수 있다
# https://medium.com/@lazysoul/functional-programming-%EC%97%90%EC%84%9C-1%EA%B8%89-%EA%B0%9D%EC%B2%B4%EB%9E%80-ba1aeb048059
f = print_hello
f()

# 함수가 일급 객체로 취급되며 closure도 사용할 수 있다
def outer(n):
    def inner():
        return n
    return inner

inner = outer(3)
print(inner())
# inner 함수는 outer 함수의 지역변수인 n을 참조한다
# outer로 전달한 파라미터 n은, inner 함수를 리턴하며 outer가 종료됨과 동시에 사라지지 않고 그대로 남아있다는 것이다
# http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%B4%EB%A1%9C%EC%A0%80-closure/

def s(a, b):
    # 매개변수를 가진 함수
    # 위치 인자라고 부른다
    return a + b

print(s(1, 3))


def s(a=10, b=10):
    # 초기값을 선언해둘 수 있다
    # 키워드 인자라고 부른다
    return a + b

print(s(a=30))
# 키워드 인자를 이용해 일부분만 인자를 전달할 수 있다


def s(*args):
    # 가변인자로 받을 땐 *을 써주면 된다
    # 가변 위치 인자 리스트라고 부른다
    # 가변인자로 전달된 값들은 튜플로 처리된다
    _sum = 0
    for number in args:
        _sum += number

    return _sum

print(s(1, 2, 3, 4))


def f(**kwargs):
    # 가변 키워드 인자 딕셔너리라고 부른다
    # 함수 안에 명시되지 않은 키워드 인자를 개수의 제약 없이 자유롭게 정의하여 함수에 전달할 수 있다
    print(kwargs['some_param'])

f(some_param=3)

# 따라서 파이썬에서 함수의 인자는 4가지로 분류된다
# 1. 위치 인자
# 2. 키워드 인자
# 3. 가변 위치 인자 리스트
# 4. 가변 키워드 인자 딕셔너리


def docstring_sample_sum(a, b):
    # 함수에는 docstring이라는 방식의 주석이 있는데, 이를 통해 문서화를 시켜줄 수 있다
    # Summary, 파라미터 정보, 리턴 정보 등을 담는다
    """
    returns a + b

    :param a: First element to sum
    :param b: Second element to sum
    :type a: int
    :type b: int

    :return: a+ b
    :rtype: int
    """
    # 생활화하자. 잘 쓰면 같이 프로젝트 하는 친구들한테 사랑받을 수 있다

    return a + b

print(docstring_sample_sum(1, 2))
