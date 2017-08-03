# 이거 배우면 코드를 좀 짜임새 있게 짤 수 있다
# 함수(function)이라는 걸 알아보기로 하자
# 사실 print라는 것도 하나의 함수다
print('hello world')
# 얘네는 builtin function이라고 부른다. 언어 설계 과정에서 만들어진 거
# 사용자 정의 함수를 선언하는 방법을 알아야 한다


def print_hello():
    print('Hello')
# 함수 선언은 def
# 함수 이름은 PEP8 표준에 따라 snake case
# 함수의 리턴은 있을 수도 있고 없을 수도 있다
print_hello()


def s(a, b):
    return a + b
# 매개변수를 가진 함수는 그냥 안에 변수 이름 써주면 된다
# 리턴은 그냥 return 쓰면 된다
print(s(1, 3))


def s(a=10, b=10):
    return a + b
# 초기값을 선언해둘 수 있다
print(s(a=30))
# 매개변수 전달은 일부분만 할 수 있다


def s3(*numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum
# 가변인자로 받을 땐 *을 써주면 된다
# 가변인자로 전달된 값들은 튜플로 처리된다
print(s3(1, 2, 3, 4))
