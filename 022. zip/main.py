list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# 파이썬의 내장 함수인 zip()을 이용해 여러 iterable 객체들을 한번에 순회할 수 있다
# 아래는 python 공식 API reference에 있는 zip() 함수를 그대로 _zip()이라는 이름의 함수로 옮겨봤다
# 이해가 힘들겠지만 한번쯤 봐두면 좋다
def _zip(*iterables):
    # iterable이라는 가변인자 변수를 이용해서, 전달되는 1개 이상의 iterable 객체를 튜플로 묶고
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    # next() 함수를 적용할 수 있도록 iterator 타입으로 만들어준 다음
    while iterators:
        # iterator가 더이상 없을 때까지 돌리며
        result = []
        for it in iterators:
            # iterator 타입으로 변환된 iterable 객체 각각에 대해서
            elem = next(it, sentinel)
            # 다음 엘리먼트를 꺼내오고
            if elem is sentinel:
                return
            result.append(elem)
            # result에 append
        yield tuple(result)
        # tuple로 만들어 yield(generator 방식 구현)

for a, b in zip(list1, list2):
    print(a, b)

# 두 리스트의 길이가 다르다면
del list2[0]

for a, b in zip(list1, list2):
    print(a, b)

# 짧은 iterable 객체를 기준으로 for가 돌아간다. 이를 해결하기 위해 itertools의 zip_longest 함수를 사용한다
from itertools import zip_longest

for a, b in zip_longest(list1, list2):
    print(a, b)

# 짧은 iterable 객체의 남은 자리는 None으로 채워진다
