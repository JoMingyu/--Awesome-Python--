# Python은 멀티 패러다임 언어이며, 함수형 프로그래밍도 지원한다
# 빌트인 함수 map(), filter()를 사용할 수 있다
# reduce는 Python 3에서 functools 모듈로 이동되었으므로, 여기서는 설명하지 않는다
l = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, l)))
# [1, 4, 9, 16, 25]

print(list(filter(lambda x: x % 2, l)))
# [1, 3, 5]

# 위의 두 코드는 아래처럼 List comprehension으로도 표현할 수 있다
print([x ** 2 for x in l])
print([x for x in l if x % 2])
# 과반수의 파이썬 개발자들은 lambda를 사용한 코드보단 comprehension을 지향한다