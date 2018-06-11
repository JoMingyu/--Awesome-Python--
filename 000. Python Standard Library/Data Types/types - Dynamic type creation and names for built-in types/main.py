# https://docs.python.org/3/library/types.html
from types import *
# https://github.com/python/cpython/blob/3.6/Lib/types.py
# 동적으로 타입을 생성하는 유틸리티이면서, Python 빌트인 타입들에 대한 wrapper

f = lambda a: a
print(isinstance(f, FunctionType))
# True
print(isinstance(f, LambdaType))
# True

def gen():
    yield 1

print(isinstance(gen(), GeneratorType))
# True
print(isinstance(sum, BuiltinFunctionType))
# True