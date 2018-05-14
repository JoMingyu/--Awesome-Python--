# 함수 안에 함수를 선언할 수 있다
def get_sum_function():
    def sum(a, b):
        return a + b

    return sum
    # 내부 함수인 sum을 반환

sum = get_sum_function()
print(sum(1, 3))
# 4

def get_number_printer(n):
    def print_n():
        print(n)
        # 내부 함수에서 외부 함수의 지역변수인 n에 참조

    return print_n

print_n = get_number_printer(3)
print_n()
# 정상적으로 외부 함수의 지역변수에 접근할 수 있음
# 이는 내부 함수인 print_n을 반환하며 외부 함수가 종료됨가 동시에 사라지지 않고 지역변수가 그대로 남아있기 때문
# 이를 closure라고 부름
