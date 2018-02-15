# Generator는 iterator를 생성해주는 function. next() 메소드를 이용해 순차적으로 접근 가능하기 때문에
# lazy(게으름)을 구현할 수 있어서 Comprehension이 클 경우 Generator를 사용하곤 한다
# 일반적인 함수와 비슷하게 보이지만, 가장 큰 차이점은 yield 구문일 것이다

def generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

# 일반적인 함수는 사용이 종료되면 결과값을 반환 후 함수를 종료시키고 메모리에서 clear
# generator 함수는 실행 중 yield를 만날 경우, 해당 함수는 그 상태로 next() 호출 시까지 정지

for x in generator(5):
    print(x)

# 위와 같은 generator 함수를 좀 더 쉽게 사용할 수 있도록 generator expression을 제공한다
# comprehension과 비슷하고, ()를 사용하면 된다
gen = (i for i in range(10))
print(next(gen))
print(next(gen))
