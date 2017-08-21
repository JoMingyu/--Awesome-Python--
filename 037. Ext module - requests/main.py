import requests
# 간단한 HTTP 요청을 위한 모듈
# pip install requests

# request 함수가 있으나 메소드 명시하는 게 좋다
response = requests.get('http://naver.com')

# response 객체가 있다. 여기서 여러가지 데이터들을 뜯어올 수 있다
print(response.content)
