# Python의 삼항 연산자는 다른 언어들이 사용하는 [condition] ? [expr_when_true] : [expr_when_false] 형태가 아닌
# if문을 사용하는 문법을 가지고 있다

print('condition is true' if '' else 'condition is false') # 'condition is true'
# [expr_when_true] if [condition] else [expr_when_false]
# 삼항 연산자는 Python 2.5 이상 버전부터 지원된다

# -

# PEP 572에서 Assignment Expression이라는 이름으로 walrus operator가 소개되었다
# Python 3.8부터 사용할 수 있으며. Go언어와 매우 유사하다

if (n := len('PlanB')) > 3:
    # [name] := [expr] 형태의 문법을 사용해,
    # block의 entry point에서 해당 block에 대한 지역변수를 정의할 때 사용할 수 있다
    print(f'Length is too long ({n} elements, expected <= 2)')
