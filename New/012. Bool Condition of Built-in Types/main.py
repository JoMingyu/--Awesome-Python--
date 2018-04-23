# Python의 모든 객체에는 참과 거짓이 존재하며
# bool() 함수를 이용해 간단히 객체의 참과 거짓을 식별할 수 있다

print(bool(1), bool(-1.0), bool(0), bool(0.0))
# True True False False
# - 정수 0과 실수 0.0은 False, 나머지는 모두 True

print(bool('PlanB'), bool(''))
# True False
# - 빈 문자열은 False, 나머지는 모두 True

print(bool(b'PlanB'), bool(b''))
# True False
# - 빈 bytes는 False, 나머지는 모두 True

print(bool(None))
# False
# - None은 False

# -- Iterable은 비어 있으면 False, 비어 있지 않으면 True
print(bool([1]), bool([]))
# True False
# - 빈 리스트는 False, 나머지는 모두 True

print(bool((1,)), bool(()))
# True False
# - 빈 튜플은 False, 나머지는 모두 True

print(bool({1: 10}), bool({}))
# True False
# - 빈 딕셔너리는 False, 나머지는 모두 True

print(bool({1}), bool(set()))
# True False
# - 빈 집합은 False, 나머지는 모두 True
