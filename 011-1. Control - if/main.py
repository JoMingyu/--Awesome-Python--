# 구조적으로 프로그래밍을 하기 위해 필요한 조건문
# 1. if - elif - else 형태로 조건분기를 구성한다
# 2. if 안에 소괄호를 씌우지 않는다
# 3. 중괄호가 아니라 콜론과 indent로 블럭을 구분한다

if True:
    print('True')

# 기본 비교 연산자는 다른 언어들이랑 똑같다(<, >, =<, => 등등)
# 논리 연산자는 조금 다르다(and, or, not)

if True or False:
    print('True of False')

if not False:
    print('not False')

if False and False:
    print('False and False')

# Iterable data 안에 특정 값이 들어 있는지 체크할 수가 있다(in/not in)
lst = [1, 2, 3]
if 4 in lst:
    print('4 in list!')
elif 3 not in lst:
    print('3 not in list!')
elif 1 in lst:
    print('1 in list!')
else:
    print("I don't know")

# 파이썬에는 ternary operator(삼항 연산자)가 if에 있다
value = 4
print('홀수' if value % 2 else '짝수')
# condition_is_true if condition else condition_is_false

# 광범위하게 사용되지 않는 ternary operator 문법이 하나 더 있는데, 튜플을 포함하고 있다
print(False, True)[True]
# tupled ternary라고 부름
# (condition_is_false, condition_is_true)[condition]
# true condition과 false condition을 넣을 자리를 혼동하기 쉬움
