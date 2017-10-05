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

# if에는 ternary operator라는 개념이 있는데, 삼항 연산과 비슷하게 이해하면 된다
value = 4
print('홀수' if value % 2 else '짝수')
