# https://docs.python.org/3/library/keyword.html
import keyword
# https://github.com/python/cpython/blob/3.6/Lib/keyword.py
# 파이썬 프로그램이, 특정 문자열이 키워드인지를 결정(determine)하게 함

print(keyword.kwlist)
# 키워드 리스트

print(keyword.iskeyword('in'))
# True
# 해당 문자열이 키워드인지를 검사

print(keyword.iskeyword('Is'))
# frozenset(keyword.kwlist).__contains__ 함수를 간접적으로 호출