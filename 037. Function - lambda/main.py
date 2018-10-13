# Python에서 def로 정의하는 함수는, 함수 선언식만 가능하고 표현식(변수에 대입하는 방식으로 선언)이 불가능하다
# lambda는 def와 동일하게 '함수를 정의'하기 위해 사용되는데, inline으로 선언 가능하다는 점이 특징이다
# 따라서 함수 표현식을 사용할 수 있게 되고, 익명 함수와 즉시 실행 함수로 사용할 수도 있다

sum = lambda a, b: a + b
# lambda (arguments...): [return statement]
# 함수 표현식
print(sum(1, 3)) # 4


def calc(func, a, b):
    return func(a, b)

print(calc(lambda a, b: a + b, 1, 3)) # 4
# 함수를 익명 생성하여 전달

print((lambda: 'hello')()) # 'hello'
# 인자가 없는 lambda 함수를 익명 생성하고, 즉시 실행
