# https://github.com/requests/requests
# pip install requests
import requests
# urllib의 사용성을 개선한 HTTP 요청을 위한 모듈

# method 인자를 받는 request 함수가 있으나 HTTP 메소드 형태로 된 함수를 호출하는 것이 더 직관적이다
response = requests.get('http://naver.com')

# response 객체가 있다. 여기서 여러가지 데이터들을 뜯어올 수 있다
print(response.status_code)
print(response.content)

# 타 HTTP 메소드들도 요청 가능하다. data 파라미터에 딕셔너리 형태로 데이터를 붙일 수 있다
# 이 경우 헤더의 Content-Type은 application/x-www-form-urlencoded로 처리된다
print(requests.post('http://httpbin.org/post', data={'key': 1}).content)

# 요청 시 JSON 데이터를 전송하려면 Content-Type을 application/json으로 설정해 주어야 하는데
# JSON 데이터를 전송할 수 있는 HTTP 메소드라면 requests 측에서 json 파라미터를 제공한다
print(requests.post('http://httpbin.org/post', json={'key': 1}).content)

# 헤더는 headers 파라미터로 설정할 수 있다
print(requests.post('http://httpbin.org/post', headers={'user-agent': 'Safari/537.36'}))
