"""
Return the next item from the iterator. If default is given and the iterator
is exhausted, it is returned instead of raising StopIteration.
"""
# (이 함수를 이해하기 위해서는 iterator 의 이해가 필요하다. 또한, iter() 를 참고하는 것이 좋다. 둘 다 Awesome Python 에서 다루었으므로 참고하기를 권장한다.)

# next() 는 iterator 를 인자로 받는다.
# next() 는 객체 내부에 __next__() 를 호출하여 iterator 의 다음 요소를 검색한다.
some_li = [1, 2.0, '3']
liIter = iter(some_li)

# list 의 iterator 의 네임 스페이스에 __next__() 가 있는 것을 확인할 수 있다. __next__() 가 있으므로 next() 의 인자로 쓸 수 있다.
print(dir(liIter))

# 1
print(next(liIter))

# 2.0
print(next(liIter))

# '3'
print(next(liIter))

# StopIteration
print(next(liIter))


# 또, next() 는 iterator 다음 인자로 default 값을 줄수 있는데,
# iterator 의 다음 요소가 없을 경우, StopIteration 대신 default 값을 반환한다.

some_tu = (1, 2.0)
tuIter = iter(some_tu)

# 1
print(next(tuIter))

# 2
print(next(tuIter))

# StopIteration 대신 default 값인 '3' 을 반환한다.
print(next(tuIter, '3'))
print(next(tuIter, '3'))
print(next(tuIter, '3'))
