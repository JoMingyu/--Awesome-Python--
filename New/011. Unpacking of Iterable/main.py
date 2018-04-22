# Iterable 객체의 각 요소들을 풀어 변수에 대입할 수 있다
# 각 매칭되는 자리끼리 바인딩이 일어나게 하는 것이다
a, b, c = [1, 2, 3]
a, b, c = 1, 2, 3
a, b, c = {1: 10, 2: 20, 3: 30}
a, b, c = {1, 2, 3}
p, l, a, n, b = 'PlanB'
# Unpacking

# 이는 변수의 swap에도 사용할 수 있다
a = 1
b = 2
c = 3
a, b, c = b, c, a

a, *b, c = [1, 2, 3, 4, 5]
a, *b = 1, 2, 3, 4, 5, 6
# Python 3의 extended unpacking

print(b)
# [2, 3, 4, 5, 6]
# Unpacking 이전의 자료형에 관계없이, extended unpack된 변수에는 list로 할당