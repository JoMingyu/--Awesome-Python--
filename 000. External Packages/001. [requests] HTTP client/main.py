# urllib 기반의 간단한 HTTP 요청을 위한 모듈
# pip install requests

import requests

# request 함수가 있으나 메소드 명시하는 게 좋다
response = requests.get('http://naver.com')

# response 객체가 있다. 여기서 여러가지 데이터들을 뜯어올 수 있다
print(response.status_code)
print(response.content)

# 타 HTTP 메소드들도 요청 가능하다. data 파라미터에 딕셔너리 형태로 데이터를 붙일 수 있다
print(requests.post('http://httpbin.org/post', data={'key': 1}).content)
