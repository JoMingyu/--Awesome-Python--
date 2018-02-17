"""
Init signature: enumerate(self, /, *args, **kwargs)
Docstring:
enumerate(iterable[, start]) -> iterator for index, value of iterable

Return an enumerate object.  iterable must be another object that supports
iteration.  The enumerate object yields pairs containing a count (from
start, which defaults to zero) and a value yielded by the iterable argument.
enumerate is useful for obtaining an indexed list:
    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
"""
# enumerate()는 iterable이나 iterator 객체의 인덱스(start의 기본값은 0)와 값으로 이루어진 pair를 튜플 형태로 yield하는 enumerate 객체를 반환한다
# iterable 객체를 index 기반으로 iteration할 때 자주 사용된다
data = list(range(5))

# 1. enumerate 없이 인덱스와 값을 함께 돌린다면
for idx in range(len(data)):
    # iterable 객체의 length를 그대로 range로 돌려야 한다
    print(idx, data[idx])

# 2. enumerate로 인덱스와 값을 함께 돌린다면
for idx, item in enumerate(data):
    print(idx, item)

# 3. start를 함께 지정
for idx, item in enumerate(data, 1):
    print(idx, item)

# --- Pure Python과 generator로 enumerate() 함수를 표현한다면

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
