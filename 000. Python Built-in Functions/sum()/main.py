""" Return the sum of a 'start' value (default: 0) plus an iterable of numbers """

# sum() 함수는 매우 간단하면서 유용한 함수이다.
# 인자로 들어온 iterable 요소들의 총합을 반환한다.
# 선택적 인자로 start 를 넣을 수 있는데, start 의 값부터 더한다. 즉, start 와 iterable의 총합을 더한값을 반환한다.

# 리스트 요소들의 총합인 15
print(sum([1, 2, 3, 4, 5]))

# 90 과 튜플의 총합을 더한 값인 150 반환
print(sum((10, 20, 30), 90))

# 만약, iterable이 비었을 경우 start 인자의 값을 반환한다.
print(sum([], 20))

# start 인자의 디폴트 값은 0이다.
print(sum([]))

# 인수로 들어오는 값은 숫자여야만 하고
# 만약, 정확한 float 타입의 총합 계산을 원한다면 math.fsum() 함수를 사용해야한다.
# 또한, 인자로 들어온 이터레이블의 요소 연결시키고 싶다면 ''.join() 함수를 사용한다.
