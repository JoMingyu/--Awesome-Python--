# 실행 비용이 비싼 함수를 호출한다고 생각해 보자
# 동일한 입력을 했을 때 동일한 결과를 반환하는 함수인 경우에는 대부분 데코레이터 형태로 메모이제이션을 사용하는 것을 선호한다
# 이 데코레이터는 이전에 실행한 적이 있는 경우에는 동일한 결과를 빠르게 내놓을 수 있도록 캐시해둔다
import time

def memoize(func):
    # memoize를 구현한 간단한 코드
    cache = {}

    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return memoizer

@memoize
def expensive_fn(a, b):
    time.sleep(3)
    return a + b

# expensive_fn 함수를 동일한 인자로 반복해서 호출하면 실제로 함수를 호출하지 않고 캐시된 값을 사용할 수 있다
before = time.time()
print(expensive_fn(1, 2))
print('First called : {}'.format(time.time() - before))

before = time.time()
print(expensive_fn(1, 2))
print('Second called : {}'.format(time.time() - before))
# expensive_fn이 호출되지 않고 캐시된 값을 바로 리턴

from functools import lru_cache
# functools.lru_cache 데코레이터를 이용해 메모이제이션 가능
@lru_cache()
def expensive_fn_2(a, b):
    time.sleep(3)
    return a + b

before = time.time()
print(expensive_fn_2(1, 2))
print('First called : {}'.format(time.time() - before))

before = time.time()
print(expensive_fn_2(1, 2))
print('Second called : {}'.format(time.time() - before))
# expensive_fn이 호출되지 않고 캐시된 값을 바로 리턴
