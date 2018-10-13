# map, filter는 Function programming의 pure function 개념이 적용된 빌트인 함수

# -- map(function, *iterables) -> map object(iterable)
# iterable의 갯수만큼 인자를 받아 하나의 결과를 반환하는 콜백 함수와
# 연산의 대상이 될 iterable 객체들을 가변 인자로 전달받아 연산의 결과를 map 객체로 반환
print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))) # [2, 4, 6, 8, 10]
# map 객체는 iterable하기 때문에 다른 iterable로 캐스팅 가능
print(list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))) # [5, 7, 9]
# 여러 iterable을 하나로 mapping

# -- filter(function or None, iterable) -> filter object(iterable)
# 하나의 인자를 받아 결과에 포함시킬지/포함시키지 않을지에 대한 boolean 값을 반환하는 콜백 함수와
# 연산의 대상이 될 iterable 객체를 인자로 전달받아 연산의 결과를 filter 객체로 반환
print(list(filter(lambda x: x > 3, [1, 2, 3, 4, 5]))) # [4, 5]
print(list(filter(None, [1, 2, 3]))) # [1, 2, 3]
# function에 None을 전달할 수도 있고, 이는 아무런 필터링도 하지 않음
