# 크롤링 준비 1번째 - urllib
# 파이썬 내장 패키지
# https://docs.python.org/3.4/library/urllib.html
from urllib.request import urlopen
# urllib은 여러가지 용도로 사용 가능하지만 간단한 크롤링에서는 urllib 정도면 충분하다

data = urlopen('http://www.naver.com', data=None)
# data 파라미터에 딕셔너리를 전달하여 query string을 표현할 수 있다
print(data.status)
print(data.read().decode('utf-8'))
# read로 데이터를 가져올 수 있음
# 유니코드로 데이터가 오기 때문에 decode 과정이 필요
