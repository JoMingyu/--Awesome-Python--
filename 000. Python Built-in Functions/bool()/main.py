"""
The bool() method converts a value to Boolean (True or False)
using the standard truth testing procedure.
"""

# bool() 함수는 인자에 따라 불리언 값. 즉, True 나 False 를 반환한다.
# bool() 함수는  'truth value testing' 를 사용하여 인자를 불리언으로 반환하는데
# 여기서 'truth value testing' 란,
# 어느 객체라도 if 나 while 같은 제어문의 조건으로 쓰이거나, 불리언 연산의 피연산자들로 사용될 때 불리언 값으로 처리된다는 개념이다.

# 파이썬에서 어떤 값들이 False 로 반환되는지 알아보자

# 일단 0을 의미하는 것들은 모두 False 이다. 정수이든, 실수이든, 복소수이든
print(bool(0))
print(bool(0.0))
print(bool(0.j))

# 빈 시퀀스들도 모두 False
print(bool([]))
print(bool(()))
print(bool(''))

# 빈 mapping(dict, set) 또한 마찬가지로 False 이다.
print(bool({}))

# None 은 당연히 False
print(bool(None))

# 위의 값들을 제외하고는 True 가 반환된다.
print(bool('Any value'))
