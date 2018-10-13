l = [1, 2, 3, 4, 5]

print(l.index(1)) # 0
# .index(key)
# key가 가장 처음 발견되는 index 반환

print(l.count(1)) # 1
# .count(key)
# key가 발견되는 횟수 반환

l.append(6)
# .append(v)
# 리스트의 맨 끝에 v를 추가

l.remove(3)
# .remove(v)
# 리스트에서 가장 처음 발견되는 v를 제거

del l[0]
# del l[n]
# n번 인덱스에 있는 요소를 제거

print(l.pop()) # 6
# .pop(n=-1)
# n번 인덱스에 있는 요소를 제거하며 반환. 기본값은 -1

l.reverse()
# 리스트 뒤집기

l.sort()
# 리스트 정렬(오름차순)

l.clear()
# 리스트 비우기
