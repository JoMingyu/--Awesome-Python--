# byte stream을 표현하기 위해 bytes 타입 지원

b = b'PlanB'
# b'abcd'와 같은 표현을 사용

print(b.decode())
# 'PlanB'
# bytes 객체의 .decode() 메소드를 통해 str로 변경

print('PlanB'.encode())
# b'PlanB'
# str 객체의 .encode() 메소드를 통해 bytes로 변경