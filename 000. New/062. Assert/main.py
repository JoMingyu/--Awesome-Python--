# Assertion은 방어적 프로그래밍(Defensive Programming)을 구현하기 위한 '가정문'이다

# assert [statement]
assert isinstance(123, int)
# Assertion은 '이 statement는 여기서 True여야 함'이라는 의미를 가지며,
# 프로그램의 특정 지점에서 assert를 만날 경우, statement의 평가가 False라면 AssertionError를 raise하며 코드를 정지시킨다

# if - raise문을 사용하는 것으로도 Assertion을 흉내낼 수 있다
if isinstance(1.5, int):
    pass
else:
    raise AssertionError()

# 테스트 코드를 작성하는 경우 자주 사용된다
