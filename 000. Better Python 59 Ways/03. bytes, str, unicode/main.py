# Python 2를 마주칠 일은 그렇게 많지는 않겠지만, Python 2와 3에서 문자열과 바이트를 다루는 차이점을 알고 있는 편이 좋다
# Python 3에서는, raw 8-bit value를 다루기 위해 bytes 자료형을 사용한다
b = b'text'
# 문자열에는 str 자료형이 사용된다
s = 'text'
# 이 둘 사이의 변환은 encode()와 decode()를 사용한다
print(b.decode())
print(s.encode())

# 그러나 Python 2의 경우, raw 8-bit value에 str, 문자열에 unicode 자료형이 사용된다
# Python 2의 unicode 자료형은 Python 3에 str 자료형으로 아직 남아 있다
u = u'text'
print(u)
print(type(u))
