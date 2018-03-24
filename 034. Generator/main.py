# Generator는 iterator의 특수한 형태. next() 메소드를 이용해 순차적으로 접근 가능하기 때문에
# lazy(게으름)을 구현할 수 있어서 Comprehension이 클 경우 Generator를 사용하곤 한다
# 일반적인 함수와 비슷하게 보이지만, 가장 큰 차이점은 yield 구문일 것이다

def generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

# 일반적인 함수는 사용이 종료되면 결과값을 반환 후 함수를 종료시키고 메모리에서 clear
# generator 함수는 실행 중 yield를 만날 경우, 해당 함수는 그 상태로 next() 호출 시까지 정지
# 따라서 원하는 시점에 데이터를 받을 수 있게 됨

for x in generator(5):
    print(x)

# 위와 같은 generator 함수를 좀 더 쉽게 사용할 수 있도록 generator expression을 제공한다
# comprehension과 비슷하고, ()를 사용하면 된다
gen = (i for i in range(10))
print(next(gen))
print(next(gen))

# iterator는 next()로 다음 요소를 순차 접근할 수 있는 데이터를 말하며
# 파이썬의 대표적인 iterable 객체는 dictionary, list는 next()가 불가능하므로 iterator는 아님
