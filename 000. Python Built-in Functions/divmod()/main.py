""" Return the tuple (x//y, x%y).  Invariant: div*y + mod == x. """
import math

# divmod 함수는 첫번째 인자(a)를 두번째 인자(b)로 나누어 리턴하는 함수 입니다
# divmod 함수의 리턴값은 요소가 2개인 튜플 형태이다
# 튜플의 첫번째 요소는 a를 b로 나눈 값이고, 두번째 요소는 a를 b로 나누었을 때 나머지값이다.
# divmod 함수의 인자는 non-complex 즉, 복소수가 아니여야 한다.

# 두 인자가 모두 int 일 경우 (a/b, a%b)
print(divmod(6, 2))
print(divmod(5, 3))

# 둘 중 하나가 float 형이면 튜플의 요소들이 float 일 경우
# 두번째 요소는 int 일 경우와 같지만 첫번째 요소는 소수점 아래가 제거된다.
# 이 경우의 튜플의 첫번째 요소는 math.floor(a/b) 의 값과 유사하다.
print(divmod(9.0, 2))
print(divmod(10, 3.0))
print(divmod(90.33, 21.35))

res = divmod(5.33, 2.3)
print(res[0])
print(math.floor(5.33 / 2.3))
