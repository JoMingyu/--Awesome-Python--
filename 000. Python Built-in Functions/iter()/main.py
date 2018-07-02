"""Get an iterator from an object."""
# (이 함수를 이해하기 위해서는 iterator 와 next() 의 이해가 필요하다. 둘 다 Awesome Python 에서 다루었으므로 선행하기를 권장한다.)

# iter() 는 iterator 객체를 반환하는 함수이다.
# iter() 의 첫번째 인자는 두번째 인자의 존재에 따라 다르게 해석된다.

# 두번째 인자가 없을 경우,
# 첫번째 인자는 __iter__() 를 가지고 있는 iteration 객체이거나,
# __getitem__() 을 가지고 있는 Sequence 객체여야 한다. 그렇지 않으면 TypeError 를 발생시킨다.

# iteration 이자 sequence 인 List 의 경우이다.
# List 처럼 python 에서 지원하는 객체들 뿐만 아니라, 조건을 충족하는 커스텀 객체도 마찬가지이다.
some_li = ['g', 'o', 'o', 'd']
liIter = iter(some_li)

# g
print(next(liIter))

# o
print(next(liIter))

# o
print(next(liIter))

# d
print(next(liIter))

# d 가 마지막 요소였으므로 next() 를 호출하면 StopIteration 이 발생한다.
print(next(liIter))


# 두번째 인자가 있을 경우,
# 호출가능한 객체여야한다.
# 두번째 인자는 sentinel 이라고 부르는데 이를 지정한 경우 __next__() 를 계속 호출하면서 값이 sentinel 과 같아지면 StopIteration 을 발생시킨다.

# 다음은 python 공식 문서 iter() 부분에 나와있는 예시이다.
# 이 예시는 iter() 를 호출할 때 sentinel 이 있는 경우를 가장 이해하기 쉽게 표현한 예시이다.
# awesome_python.txt 를 sentinel character 인 '' 에 도달할때까지 루프를 돌며 읽는 코드이다.
with open('awesome_python.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)
