# https://docs.python.org/3.6/library/string.html
import string
# https://github.com/python/cpython/blob/3.6/Lib/string.py
# 일반적인 문자열에 대한 작업들을 위한 모듈이다

print(string.ascii_letters)
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(string.ascii_lowercase)
# 'abcdefghijklmnopqrstuvwxyz'

print(string.ascii_uppercase)
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(string.digits)
# '0123456789'

print(string.hexdigits)
# '0123456789abcdefABCDEF'

print(string.octdigits)
# '01234567'

# string.Formatter 클래스를 이용해 커스텀 문자열 포매팅을 구현할 수도 있다