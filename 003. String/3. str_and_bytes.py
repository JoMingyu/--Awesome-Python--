byte_data = b'hello'
# 바이트 데이터를 표현하려면 b를 붙이면 된다

str_data = 'hello'
# 문자열은 우리가 알던 대로

print(type(byte_data))
# bytes

print(type(str_data))
# str

print(str_data.encode('utf-8'))
# 문자열 -> bytes는 encode
print(byte_data.decode('utf-8'))
# bytes -> 문자열은 decode를 사용한다

print(str_data.encode('utf-8').decode('ms949'))
