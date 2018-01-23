# input의 리턴은 모두 str이다. 확인해 보자
num = input('입력 > ')
print(type(num))

# 파이썬은 빌트인을 통해 손쉽게 타입 캐스팅이 가능하다
num = int(num)
print(type(num))
# 실제로 타입이 바뀐 걸 볼 수가 있다. 캐스팅에 문제가 있으면 ValueError가 발생한다(str('a') 등)

str()
int()
float()
bytes()
bytearray()

# 대표적인 타입 캐스팅 사례
dic = {'key1': 1, 'key2': 2}
print(list(dic.keys()))
