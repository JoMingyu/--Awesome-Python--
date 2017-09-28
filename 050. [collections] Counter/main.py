import collections

_list = [1, 2, 3, 3, 2, 4, 5, 3, 3]
# 리스트 내의 요소가 몇 번이나 반복되었는지 카운트할 경우가 생긴다

counter = collections.Counter(_list)
print(counter)
print(counter[3])
print(counter.most_common(2))
