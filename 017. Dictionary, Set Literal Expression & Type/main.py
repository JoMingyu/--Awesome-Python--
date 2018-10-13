# Dictionary는 key-value mapping을, Set은 중복 불가능한 값의 집합을 표현한다
# Iterable이라는 점은 리스트/튜플과 동일하고, 순서가 보장되지 않으므로 Sequence는 아니다

# -- Dictionary
{'nickname': 'PlanB', 'region': 'Seoul'}
# {k: v, k: v, ...}
# key는 해시 가능하며 동일(==) 연산자의 적용이 가능한 객체만, value는 어떤 객체든 사용 가능하다
# -> Dictionary는 key의 유일성을 보장하므로, 중복 체크를 위해 해시 가능해야 함

d = {1: 2}
print(d[1]) # 2
# Sequence 객체들의 인덱싱과 비슷한 형태로 값을 가져올 수 있다
# 그러나 Sequence와 다르게, 인덱스가 아닌 key를 의미한다는 것에 차이가 있다

# -- Set
{1, 2, 3, 4, 5}
# {v, v, v, ...}
# 중괄호로 감싸는 건 Dictionary와 동일하고, 값만을 나열한다는 것의 차이

# Set은 실제로 수학의 집합처럼 사용할 수 있다
print({1, 2, 3} & {2, 4, 5}) # {2}
# 교집합

print({1, 2, 3} | {2, 4, 5}) # {1, 2, 3, 4, 5}
# 합집합

print({1, 2, 3} - {3, 4}) # {1, 2}
# 차집합

# 순서가 보장되지 않으며, Dictionary처럼 key가 있는 것도 아니기 때문에 요소의 임의 접근 불가능
