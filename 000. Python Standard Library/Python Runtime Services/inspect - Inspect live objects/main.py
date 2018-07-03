# https://docs.python.org/3/library/inspect.html
from inspect import *
# https://github.com/python/cpython/blob/3.6/Lib/inspect.py
# Python의 객체들을 확인(inspection)하기 위해 사용
# types 모듈에 많이 의존하고 있다
import another

print(ismodule(another))
# True
# print(isinstance(another, types.ModuleType))와 동일

class C:
    def func(self):
        pass

print(isclass(C))
# True
print(isfunction(C.func))
# True
print(ismethod(C().func))
# True

def gen():
    l = list(range(10))

    for item in l:
        yield item

print(isfunction(gen))
# True
print(isgeneratorfunction(gen))
# True
print(isgenerator(gen()))
# True

async def gen():
    yield 1

print(isasyncgenfunction(gen))
# True

# 위와 같은 단순한 타입 검사, 함수 시그니처 검사, 파라미터 검사 등을 수행할 수 있다
