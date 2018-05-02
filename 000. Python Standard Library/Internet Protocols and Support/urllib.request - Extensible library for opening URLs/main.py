# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# URL open을 위한 확장 가능한 라이브러리
from urllib.request import urlopen, Request
import ssl

def get_ssl_context(url):
    # https 주소로 접속할 때 ssl context를 생성하기 위함
    return ssl._create_unverified_context()

res = urlopen('https://github.com/JoMingyu', context=get_ssl_context())
# http.client.HTTPResponse 객체가 반환됨

print(res.getcode())
# 응답의 HTTP status code
print(res.read(100).decode('utf-8'))
# read(cnt)는 cnt byte만큼 데이터를 읽어오고, cnt를 전달하지 않으면 처음부터 끝까지 읽음
# bytes 타입이기 때문에 utf-8로 decode

req = Request('https://github.com/JoMingyu', headers={'Content-Type': 'text/plain'}, method='GET')
# Request 인스턴스를 이용해 요청 객체를 생성. 헤더나 메소드 등을 명시할 수 있음
# Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

print(req.full_url)
# https://github.com/JoMingyu
print(req.type)
# https
print(req.host)
# github.com
print(req.get_method())
# GET
print(req.header_items())
# [('Content-type', 'text/plain')]
# ...

res = get_redirected_url(req)
# urlopen은 Request 인스턴스도 허용

print(res.getcode())
print(res.read(100).decode('utf-8'))
