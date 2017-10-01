# pip install PyJWT
# 이 패키지를 이용해서 JWT 토큰을 만들어낼 수 있다
import jwt

encoded = jwt.encode({'some': 'payload'}, 'secret!@@#*!#', 'HS256')
# bytes를 반환

print(encoded)
print(encoded.decode('utf-8'))
# 문자열로 바꾸기

# https://jwt.io/
# 겨우 저 한줄만으로 헤더, 페이로드, 시그니처가 포함된 완전한 JWT 토큰이 만들어졌다

print(jwt.decode(encoded, 'secret!@@#*!#', 'HS256'))
# 토큰을 decode해서 페이로드를 받아오는 부분
# 자동으로 dict 반환 해준다
