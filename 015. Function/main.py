# 함수를 통해 코드를 좀 짜임새 있게 짤 수 있다
# print라는 것도 하나의 함수다
print('hello world')
# 얘네는 builtin function이라고 부른다. 언어 설계 과정에서 만들어진 함수들
# 사용자 정의 함수를 선언하는 방법을 알아야 한다


def print_hello():
    # 함수 선언은 def
    # 함수 이름은 PEP8 표준에 따라 snake case
    print('Hello')
    # 함수의 리턴은 있을 수도 있고 없을 수도 있다

print_hello()


def s(a, b):
    # 매개변수를 가진 함수
    return a + b

print(s(1, 3))


def s(a=10, b=10):
    # 초기값을 선언해둘 수 있다
    # 선택적 인자라고 부른다
    return a + b

print(s(a=30))
# 매개변수 전달은 일부분만 할 수 있다


def s3(*numbers):
    # 가변인자로 받을 땐 *을 써주면 된다
    # 가변인자로 전달된 값들은 튜플로 처리된다
    _sum = 0
    for number in numbers:
        _sum += number

    return _sum

print(s3(1, 2, 3, 4))


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
    # 잘 쓰면 프로젝트 하는 친구들한테 사랑받을 수 있다

    return a + b

print(docstring_sample_sum(1, 2))
