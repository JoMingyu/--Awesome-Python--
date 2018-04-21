# Dictionary와 Set은 List, Tuple처럼 Iterable 객체지만 순서가 보장되어 있지는 않음

# -- Dictionary
d = {1: 10, 2: 20}
# 중괄호로 감싸고, 각 쌍은 쉼표로 구분
# Dictionary는 임의의 키가 값에 매핑되는 연관 배열

d = {(1, 2): 10}
# key는 __hash__() 및 __eq__() 메소드가 있는 객체를, value는 어떤 자료형이든 사용 가능

# 1. 요소 추가
d[3] = 30
d['nickname'] = 'PlanB'
# List의 인덱싱과 유사

# 2. 요소 접근
print(d[3])
# 30

# 3. 요소 수정
d[3] = 40
# 수정하고자 하는 key에 접근하여 value를 덮어써주면 됨

# 4. 요소 제거
del d[3]

# 5. 기타 메소드
print(d.keys())
# 딕셔너리의 key만 리스트로 반환
print(d.values())
# 딕셔너리의 value만 리스트로 반환
print(d.items())
# 딕셔너리의 item들을 (key, value) 형태의 튜플로 이루어진 리스트로 반환

d.update({1: 10, 2: 20})
# dictionary.update(dictionary_new) -> dictionary에 dictionary_new를 덮어씀

print(d.pop(1))
# dictionary.pop(k) -> dictionary[k]에 해당하는 요소를 제거하며 반환

d.clear()
# dictionary.clear() -> 딕셔너리의 요소를 모두 제거

# -- Set
s = {1, 2, 3, 4, 5, 5}
# 중괄호로 감싸며, 각 요소는 쉼표로 구분
# Set은 수학의 집합과 유사함

print(s)
# {1, 2, 3, 4, 5}
# Set은 중복을 허용하지 않기 때문에, 할당 과정에서 중복이 제거됨

s2 = {1, 2, 5}

# 실제로 수학의 집합처럼 사용 가능

print(s & s2)
# {1, 2, 5}
# 교집합

print(s | s2)
# {1, 2, 3, 4, 5}
# 합집합

print(s - s2)
# {3, 4}
# 차집합

# 1. 요소 추가
s.add(8)

# 2. 요소 제거
s.remove(2)

# 순서가 보장되지 않고, Dictionary처럼 key가 있는 것도 아니기 때문에 요소 접근과 수정은 불가능