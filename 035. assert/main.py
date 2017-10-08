# Assert는 대부분의 프로그래밍 언어에서 지원한다
# 방어적 프로그래밍(defensive programming)에서 사용하며 코드를 점검하는 데 사용된다

# 기본적으로 assert [condition]의 구문을 사용한다
# condition이 False이면 AssertionError를 발생시킨다
assert type(123) == int
# assert isinstance(1.5, int)

# unittest 모듈의 assertEquals, assertTrue 등의 메소드가 있다. 바로 다음에서 알아보자
