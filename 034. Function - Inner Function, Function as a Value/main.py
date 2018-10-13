# Python에서 함수는 하나의 객체이며, 따라서 값으로서 변수에 할당 가능하다

def sum(a, b):
    return a + b

s = sum
# 함수가 값임을 활용한 aliasing(별명 짓기)
print(s(1, 3)) # 4

def get_sum_function():
    def sum(a=0, b=0):
        # Python은 함수 안에 함수를 정의할 수 있으며
        return a + b

    return sum
    # 반환값으로 함수를 사용할 수 있고

def calc(func, a, b):
    # 함수의 인자가 함수가 될 수도 있다
    return func(a, b)

s_func = get_sum_function()
print(calc(s_func, 1, 3)) # 4
# * get_sum_function과 calc 함수처럼,
# 함수를 인자로 전달받거나 함수를 반환하는 함수를 higher-order function이라고 부른다
