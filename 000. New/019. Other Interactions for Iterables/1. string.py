s = 'hello'

print(s.count('l')) # 2
# .count(key)
# key가 문자열에 등장하는 횟수를 반환

print(s.replace('l', 'e')) # 'heeeo'
# .replace(old, new)
# 문자열의 old를 new로 바꾼 결과를 반환

print(s.split('e')) # ['h', 'llo]
# .split(key)
# key를 기준으로 문자열을 잘라낸 결과를 list로 반환

print(s.strip('o')) # 'hell'
# .strip(key)
# key를 문자열 양 쪽에서 없앤 결과를 반환
# 문자열의 양 쪽에서 공백을 제거하는 경우 자주 사용됨

print('.'.join(s)) # 'h.e.l.l.o'
# .join(iterable)
# iterable의 요소마다 해당 문자열 객체를 삽입한 결과를 반환

print(s.startswith('he')) # True
print(s.endswith('l')) # False
# .startswith(key)
# .endswith(key)
# 해당 문자열이 key로 시작하는지/끝나는지를 반환
