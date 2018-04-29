# 아래와 같은 if statement는 삼항 연산자로 변경 가능하다
flag = True
msg = ''

if flag:
    msg = 'flag is True'
else:
    msg = 'flag is False'

print(msg)
# flag의 boolean 평가에 따라 msg가 달라지는 형태

# Python의 삼항 연산자는 문법적으로 if문을 사용한다. Python 2.5 이상부터 사용할 수 있다
print('flag is True' if flag else 'flag is False')
# [expr_when_cond_is_true] if [condition] else [expr_when_cond_is_false]
