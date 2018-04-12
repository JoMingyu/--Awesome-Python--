""" With two or more arguments, return the largest argument. """
""" With a single iterable argument, return its biggest item. """

# max() 함수는 이름에서도 알 수 있듯이 '가장 큰 값' 을 반환하는 함수이다.
# max() 는 인자의 종류에 따라 여러가지 방법으로 쓰이는데

# 이터레이블 객체가 들어왔을 시, 요소 중 가장 큰 값을 반환한다.
print(max([1, 3, 5, 7, 9]))

# default 인자는 이터레이블 객체가 비어있을 경우 반환되는 값을 설정할 수 있게 해준다.
print(max([], default=3))

# 이터레이블이 아닌 인자들이 들어왔을 때, 인자들 중 가장 큰 값을 반환한다.
print(max(1, 5, 3, 6))

# max() 에는 key 라는 선택적 인자가 있는데, key 에는 헬퍼 함수를 넣는다.
# max() 로 들어온 인자들을 헬퍼 함수의 인자로 하여 그 반환값 중 최댓값을 구한다.


def sum_digits(num):
    sum = 0
    while(num != 0):
        sum += num % 10
        num = num / 10
    return sum


# 자리수를 더해주는 헬퍼 함수를 key 로 하여 max() 의 결과는 55가 된다.
print(max(55, 12, 301, 2100, key=sum_digits))
