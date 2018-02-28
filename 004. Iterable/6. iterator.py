# list, tuple, dictionary같은 것들은 iterable 객체인데
# iterable 객체에서 실제로 iteration(반복)을 실행하는 것은 iterator
# iterator는 next 메소드를 사용하여 다음 요소를 가져오고, 더이상 next할 요소가 없으면 StopIteration Exception을 발생시킴
l = [1, 2, 3]
it = iter(l)
# 빌트인 함수 iter()를 이용해 쉽게 iterator를 만들어낼 수 있다

print(type(it))

print(next(it))
print(next(it))
print(next(it))

# 따라서 어떤 클래스를 iterable하게 만드려면, 그 클래스의 iterator를 리턴하는 __iter__() 메소드를 작성해야 하며
# iterator를 순차적으로 접근하기 위한 __next__() 메소드까지 구현해야 한다

class MyCollection:
    def __init__(self, size=10):
        self.size = size
        self.data = list(range(self.size))
 
    def __iter__(self):
        self.index = 0
        return self
 
    def __next__(self):
        if self.index >= self.size:
            raise StopIteration
 
        n = self.data[self.index]
        self.index += 1
        return n

coll = MyCollection()
for x in coll:
    print(x)
