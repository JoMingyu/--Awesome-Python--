# https://docs.python.org/3/library/timeit.html
import timeit
# https://github.com/python/cpython/blob/3.6/Lib/timeit.py
# 적은 양의 파이썬 코드의 시간을 측정할 수 있는 간단한 API를 제공
# 간단한 코드 블럭에 대한 성능 측정을 위해 사용할 수 있는 모듈

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
# 0.2832030730205588
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
# 0.25529142800951377
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))
# 0.19287355500273407
# timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000)
# 인자로 전달된 setup을 수행한 후 stmt를 number번 수행한 시간을 반환

print(timeit.repeat('[str(a) for a in range(range_count)]', setup='range_count=100', number=10000))
# [0.039610359992366284, 0.03077489702263847, 0.029420369013678282]
# timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=3, number=1000000)
# 인자로 전달된 setup을 수행한 후 stmt를 number번씩 repeat회 수행한 시간을 리스트로 반환

t = timeit.Timer('char in text', setup='text="PlanB"; char="a"')
# timeit.Timer(stmt='pass', setup='pass', timer=<timer function>, globals=None)
# Timer 객체 생성을 통해 시간 측정도 가능

print(t.timeit(number=10000000))
# 0.2807829689991195
print(t.repeat(number=10000000, repeat=5))
# [0.2838175109936856, 0.27970324497437105, 0.2810466270020697, 0.29007208699476905, 0.28556226898217574]