# Generator는 iterator를 만들어내는 함수

# iterator는 객체에 __next__()라는 매직 메소드가 구현되어 있어
# next()로 다음 요소를 순차 접근할 수 있는 객체를 말하며
# 파이썬의 대표적인 iterable 객체들(dictionary, list 등)은 __next__()가 정의되어 있지 않아 iterator는 아님
# 그러나 이들은 __iter__() 메소드가 구현되어 있고, 이는 __next__()가 구현되어 있는 iterator를 반환함
list_it = iter([1, 2, 3, 4, 5])
print(next(list_it))
# list_it.__next__()가 호출됨
print(next(list_it))
print(next(list_it))
print(next(list_it))
print(next(list_it))

# Generator는 next() 메소드를 이용해 순차적으로 접근 가능하기 때문에
# lazy(게으름)을 구현할 수 있어서 Comprehension이 클 경우 Generator를 사용하곤 한다
# 일반적인 함수와 비슷하게 보이지만, 가장 큰 차이점은 yield 구문일 것이다

def generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

# 일반적인 함수는 사용이 종료되면 결과값을 반환 후 함수를 종료시키고 메모리에서 clear
# generator 함수는 실행 중 yield를 만날 경우, 해당 함수는 그 상태로 next() 호출 시까지 정지
# 따라서 next()를 통해 yield 구문을 실행시킬 수 있어서 원하는 시점에 데이터를 받을 수 있음

gen = generator(5)
# Generator 객체 생성
print(dir(gen))
# Generator로 생성된 객체에는 __next__() 메소드가 정의되어 있음

print(next(gen))
# 0
# gen.__next__() 호출
print(next(gen))
# 1

# 위와 같은 generator 함수를 좀 더 쉽게 사용할 수 있도록 generator expression을 제공한다
# comprehension과 비슷하고, ()를 사용하면 된다
gen = (i for i in range(10))
print(next(gen))
print(next(gen))
