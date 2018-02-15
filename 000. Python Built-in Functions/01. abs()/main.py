""" Return the absolute value of the argument. """

# abs 함수는 파라미터로 전달된 숫자의 절댓값을 반환하는 함수 이다.
# 파라미터의 타입에 따라 달라지는데

# 1. <class 'int'> 의 경우, 절댓값을 반환한다.
print(abs(8))
print(abs(-2))

# 2. <class 'float'> 의 경우에도 절댓값을 반환한다.
print(abs(5.666))
print(abs(-3.18))

# 3. <class 'complex'> (복소수)의 경우, 복소수가 복소평면의 원점과 떨어진 거리를 반환한다.
# 여기서 복소평면 이란, x축이 실수축이고 y축이 허수축인 평면을 말한다.
# (파이썬에서 복소수는 i 가 아닌 j로 나타낸다)
print(abs(6j))
print(abs(-2j))
print(abs(1+1j))
