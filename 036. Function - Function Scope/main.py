# -- Python은 block에서 정의된 지역변수에 접근할 수 있다
if True:
    a = 1

print(a) # 1
# if 블록 내에서 정의된 a에 접근

# -- 반면 함수 내부의 지역변수에는 접근할 수 없다
def init():
    b = 1

init()
# print(b)
# Python은 이처럼 블록 내에 정의된 지역변수는 접근 가능하고,
# 함수 내에 정의된 지역변수는 접근 불가능한 Function Scope라는 특징을 가지고 있다
