# 반복문을 사용해 iterable 객체를 만들어내는 경우, 아래와 같은 평범한 for loop를 사용할 수 있다

l = [1, 2, 3, 4, 5]
res = []

for i in l:
    res.append(i ** 2)

# 아래는 수학에서 집합, 튜플, 벡터 등을 만들어내는 일반적인 방법이다
# S = {x² : x in {0 ... 9}}
# V = (1, 2, 4, 8, ..., 2¹²)
# M = {x | x in S and x even}
# Python은 위와 비슷한 형태의 문법으로, comprehension이라는 개념을 지원한다
# 이는 수학의 컨셉을 적용하여 쉽게 iterable 객체를 구성하는 데 사용된다

# -- List Comprehension
# [<expr> for <element> in <iterable>]
print([i ** 2 for i in l]) # [1, 4, 9, 16, 25]

# 조건문도 함께 사용할 수 있다
# [<expr_when_cond_is_true> for <element> in <iterable> if <condition>]
print([i ** 2 for i in l if i % 2]) # [1, 9, 25]
# list에서 홀수만을 골라 제곱하여 새로운 list 생성

# else 분기도 사용할 수 있는데, 이 경우 조건문과 반복문의 위치가 서로 바뀌어야 한다
# [<expr_when_cond_is_true> if <condition> else <expr_when_cond_is_false> for <element> in <iterable>]
print([i ** 2 if i % 2 else i ** 3 for i in l]) # [1, 8, 9, 64, 25]
# list에서 홀수는 제곱, 짝수는 세제곱하여 새로운 list 생성

# -- Set Comprehension
# {<expr> for <element> in <iterable>}
print({i ** 2 for i in l}) # {1, 4, 9, 16, 25}

# -- Dictionary Comprehension
# {<key_expr>:<value_expr> for <element> in <iterable>}
print({i: i ** 2 for i in l}) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Python의 대부분의 기능들은 다른 언어에서도 대충 엿볼 수 있는데, 이처럼 간단한 comprehension은 Python만 가지고 있는 강점이다
# -> Scala도 가능하긴 하지만, FP 개념이 들어가기 때문에 이처럼 간단하진 않다
# Python의 comprehension은 함수형 프로그래밍에서 filter, map, reduce를 대신할 수 있는 문법이기도 하다
