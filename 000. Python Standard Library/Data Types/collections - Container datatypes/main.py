import collections
# 범용 빌트인 컨테이너인 list, tuple, dict, set을 기반으로 한 특화된 컨테이너를 제공

# -- collections.defaultdict([default_factory[, ...]])
# dict의 서브클래스로, __getitem__이 전달된 key를 찾을 수 없는 경우 default_factory를 호출한다
d = collections.defaultdict(lambda: 0)

d['reserved'] = 10
print(d['reserved']) # 10
print(d['unknown']) # 0

d = collections.defaultdict()

# print(d['unknown']) # KeyError
# default_factory가 없는 defaultdict는 빌트인 컨테이너 dict와 별 차이가 없음

# -- collections.Counter([iterable-or-mapping])
# dict의 서브클래스로, hashable한 객체들의 카운팅을 해준다. 다른 언어에서 bag이나 multiset과 유사하다
c = collections.Counter([1, 2, 3, 3, 3, 4, 4, 5])
print(c) # Counter({3: 3, 4: 2, 1: 1, 2: 1, 5: 1})
print(c[3]) # 3

c = collections.Counter('aabbadfdbaavvbbbc')
print(c) # Counter({'b': 6, 'a': 5, 'd': 2, 'v': 2, 'f': 1, 'c': 1})
print(c.most_common(4)) # [('b', 6), ('a', 5), ('d', 2), ('v', 2)]
# collections.Counter.most_common(n)
# -> 카운트를 기준으로 내림차순 정렬하여 n개의 메트릭을 튜플로 이루어진 리스트로 반환
