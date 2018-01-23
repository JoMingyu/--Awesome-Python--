# 변수 선언은 간단하다
a = 13
# 정수형 변수 선언 : 동적 타입 언어기 때문에 단순 assign만 해주고 나면 런타임에 타입 검사를 수행한다

# 타입은 print()와 같은 built-in function인 type() 함수를 사용할 수 있다
print(type(a))
# <class 'int'>

a = 3.5
# int가 담겼던 변수에 재할당
# 소수점이 포함된 숫자는 실수형으로 분류된다
# 파이썬에서 실수는 float 타입만 사용한다
print(type(a))

a = 0.8e + 15
# e 표기법
print(a)

# e 표기법은 지수 표기법이므로 float으로 처리된다
print(type(a))

a = 0x1f
# 16진수
print(a)

a = 0o14
# 8진수
print(a)

print(5 / 2)
# 일반적인 나눗셈. 나누어 떨어지더라도 몫은 무조건 float. true div라고 말함

print(5 // 2)
# 반올림하여 몫을 int로 반환, floor div라고 말함

print(5 ** 2)
# 제곱
