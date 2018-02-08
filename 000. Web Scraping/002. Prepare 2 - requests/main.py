# 크롤링 준비 2번째 - requests
# pip install requests
import requests
# urllib 기반의 HTTP Request 라이브러리
# 사용성이 효율적으로 개선되었고, 인코딩 처리 등 여러가지 면에서 좋음

resp = requests.get('http://www.naver.com')
# get, post, delete, patch 등의 함수들이 있음

print(resp.status_code)
# Status code
print(resp.apparent_encoding)
# 해당 HTML 코드의 인코딩 방식 리턴
# 이 외 유용한 여러가지 property들이 존재

print(resp.content.decode('utf-8'))
# HTML 본문을 bytes 형태로 리턴. 유니코드 형태
print(resp.text)
# HTML 본문을 decode 처리하여 리턴. str 타입
