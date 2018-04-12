""" With a single iterable argument, return its smallest item.  """
""" With two or more arguments, return the smallest argument. """

# min() 함수는 max() 함수의 반대로 최솟값을 반환해주는 함수이다.
# min() 을 사용하는 방법은 max() 와 같다.

# 이터레이블 객체가 들어왔을 시, 요소 중 최솟값을 반환한다.
print(min([1, 3, 5, 7, 9]))

# default 인자는 이터레이블 객체가 비어있을 경우 반환되는 값을 설정할 수 있게 해준다.
print(min([], default=2))

# 이터레이블이 아닌 인자들이 들어왔을 때, 인자들 중 최솟값을 반환한다.
print(min(10, 5, 3, 6))

# min() 역시 key 라는 선택적 인자가 있는데, key 에는 헬퍼 함수를 넣는다.
# min() 로 들어온 인자들을 헬퍼 함수의 인자로 하여 그 반환값 중 최솟값을 구한다.

li1 = [1, 2, 3]
li2 = [100, 234, 663, 77, 400, 403, 747]
li3 = [2, 7, 8, 9]

# 길이를 반환하는 len() 을 key 로 하여 인자로 들어온 세 리스트 중 길이가 가장 짧은 리스트를 반환하였다.
print(min(li1, li2, li3, key=len))
