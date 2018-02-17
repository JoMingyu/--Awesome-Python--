"""
Init signature: range(self, /, *args, **kwargs)
Docstring:
range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
"""
# range()는 start에서 stop - 1 사이의 연속된 정수를 step만큼씩 더해 제공하는 range 객체를 반환
# start는 기본값이 0이며 stop은 전달하지 않으면 TypeError가 발생함
print(type(range(10)))
for i in range(10):
    print(i)

for i in range(10, 100, 5):
    # start인 10부터 stop인 100 - 1까지 5씩 더하며 yield
    print(i)

# Python2에서 range()는 yield 처리를 하지 않아 값이 커지면 느렸고, 따라서 yield 처리를 하는 xrange가 함께 있었는데
# 당시 range()에 비해 xrange()의 사용이 압도적으로 많아 Python3에선 둘을 나누지 않고 yield 처리하는 range()만을 가지고 있음

# --- Pure python과 generator로 range() 함수를 표현한다면 아래와 같은 형태

def is_valid_range(start, stop, step):
    # start보다 stop이 작은데(내림차로 range되는 경우인데) step은 양수일 경우를 필터링
    return True if (start - stop) // step < 0 else False

def pyrange1(start, stop, step):
    if is_valid_range(start, stop, step):
        # start가 2, stop이 7, step이 2인 상황이라고 쳤을 때
        # 아래의 while loop처럼 start != stop을 조건으로 해서(start <= stop을 조건으로 걸면 역방향 range()에는 대응 불가능하기 때문)
        # while을 돌리며 start를 누적시킨다면, 해당 조건식이 성립하지 않는다
        # - start가 2, 4, 6, 8, ... 형태로 나아가므로 stop과 맞지 않음
        
        # 따라서 stop을 아래 수식으로 보정해줌
        stop += (start - stop) % step
        while start != stop:
            yield start
            start += step

def pyrange2(stop):
    start = 0
    step = 1
    if is_valid_range(start, stop, step):
        stop += (start - stop) % step
        while start != stop:
            yield start
            start += step
