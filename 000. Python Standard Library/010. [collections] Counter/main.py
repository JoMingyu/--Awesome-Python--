# https://docs.python.org/3/library/collections.html
# https://www.slideshare.net/dahlmoon/collections-20160313
import collections
# 튜플과 딕셔너리에 대한 확장 데이터 구조를 제공하는 모듈
# 여러가지 요소들이 있지만, 간단하게 Counter만 알아보자

_list = [1, 2, 3, 3, 2, 4, 5, 3, 3]
# 리스트 내의 요소가 몇 번이나 반복되었는지 카운트할 경우가 생긴다

counter = collections.Counter(_list)
# collections 모듈의 Counter 클래스의 생성자에 데이터를 넘겨주자

print(counter)
print(counter[3])
print(counter.most_common(2))
