# 문자열과 bytes 간의 변환은, 문자열 객체의 encode()와 bytes 객체의 decode()를 사용한다

'hello'.encode()
# b'hello'
b'hello'.decode()
# 'hello'

# 기본 인코딩은 utf-8이며, ascii, utf-16 등 다른 종류의 인코딩을 사용할 수 있다
'hello'.encode('utf-16')
# b'\xff\xfeh\x00e\x00l\x00l\x00o\x00'
