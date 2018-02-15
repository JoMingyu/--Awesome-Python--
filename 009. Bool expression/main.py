# Python의 bool expression은 간단한 조건 검사를 할 때 유용하다
# condition or condition
# condition and condition
# ...
condition = True
print(condition or 100)

condition = False
print(condition or 100)
# 첫 번째 서브 표현식(condition)이 True면 condition을 반환하고, False라면 or 뒤의 두 번째 서브 표현식(100)을 반환한다

# 아래의 ternary operator보다 간결하다
print(condition if condition else 100)
