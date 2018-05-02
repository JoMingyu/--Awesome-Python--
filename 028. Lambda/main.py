# lambda는 익명 함수를 inline으로 선언하기 위한 키워드
sum = lambda a, b: a + b
# return statement가 없으며 반환값을 만드는 표현식만 있음
print(sum(1, 3))
# def로 정의된 함수와 동일한 역할

# lambda는 런타임에 익명으로 생성 가능하므로 아래처럼 필요한 곳에서 즉시 사용하고 버릴 수 있음
def calc(func, a, b):
    return func(a, b)

print(calc(lambda a, b: a + b, 1, 3))
# 익명 생성 가능하다는 특징 때문에 함수형 프로그래밍을 위해 자주 사용

get_msg = lambda: 'PlanB'
# 인자가 없는 lambda 함수

print(get_msg())