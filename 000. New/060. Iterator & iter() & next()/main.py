# - Iterator는 연속적인 데이터의 스트림을 나타내는 객체이며 내부에 __next__ 메소드를 구현하고 있어,
# 빌트인 함수 next()를 통해 간접적으로 해당 메소드를 호출하여 순차적인 요소의 접근이 가능한 객체를 말한다
# 따라서 next()의 반복 호출은 데이터 스트림의 항목들을 순서대로 반환하게 된다
# - __iter__ 메소드가 구현되어, 빌트인 함수 iter()에게 해당 객체의 iterator를 반환하는 객체를 Iterable이라 부른다

l = [1, 2, 3, 4, 5]
l_iter = iter(l)
# l.__iter__()
# 해당 list에 대한 Iterator 반환

print(type(l_iter)) # <class 'list_iterator'>
print(next(l_iter)) # 1
print(next(l_iter)) # 2
print(next(l_iter)) # 3
print(next(l_iter)) # 4
print(next(l_iter)) # 5
print(next(l_iter)) # StopIteration
# 반환할 데이터가 더 이상 없는 경우, StopIteration이 raise된다

# for loop에 iterable 객체를 전달하는 경우,
# Python 인터프리터는 해당 객체의 __iter__()를 호출하여 iterator를 얻어온 후 next()를 계속해서 호출하며 반복문을 수행한다
