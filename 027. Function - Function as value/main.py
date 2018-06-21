# Python의 함수는 하나의 객체이며, 따라서 값으로서 변수에 할당 가능하다
def sum(a, b):
    return a + b

s = sum
print(s(1, 3))

# 함수에 인자로 전달하거나, 반환값이 될 수도 있다
def get_sum_function():
    def sum(a=0, b=0):
        return a + b

    return sum
    # 내부 함수인 sum을 반환

def calc(func, a, b):
    # 인자로 함수와 숫자 a, b
    return func(a, b)

s_func = get_sum_function()
print(calc(s_func, 1, 3))