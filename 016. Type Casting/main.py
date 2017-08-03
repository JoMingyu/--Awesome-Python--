# 앞에서 말했듯 input의 리턴은 모두 str이다. 확인해 보자
num = input('입력 > ')
print(type(num))
# 단순히 인풋을 캐스팅해줄 필요도 있을거고 여러가지로 캐스팅할 일 진짜 많다
# Java는 wrapper class에서 parse*** 방식으로 하는데 파이썬은 빌트인이 있다
num = int(num)
print(type(num))
# 실제로 타입이 바뀐 걸 볼 수가 있다. 캐스팅에 문제가 있으면 ValueError를 뿜는다
str()
int()
float()
bytes()
bytearray()

# 대표적인 타입 캐스팅 사례는 바로 이거
dic = {'key1': 1, 'key2': 2}
print(list(dic.keys()))
