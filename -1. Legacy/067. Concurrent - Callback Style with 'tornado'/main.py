# https://github.com/tornadoweb/tornado
# pip install tornado
from tornado.httpclient import AsyncHTTPClient
from tornado import ioloop
import time
# tornado는 콜백 스타일을 사용하는 비동기 네트워크 IO 프레임워크이다
# 일반적으로 비동기 웹 서버를 구현하기 위해 사용하나, 여기서는 비동기 파이썬이 진화한 흐름을 알기 위해 AsyncHTTPClient만을 사용하자
urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def handle_response(response):
    if response.error:
        print("Error:", response.error)
    else:
        url = response.request.url
        data = response.body
        print('{} : {}...({} bytes)'.format(url, data[:10], len(data)))

    ioloop.IOLoop.current().stop()

loop = ioloop.IOLoop.current()
# event loop 생성
http_client = AsyncHTTPClient()

for url in urls:
    loop.add_callback(http_client.fetch, url, lambda resp: handle_response(resp))
    # event loop에 콜백 추가 : add_callback(func, args, lambda)
    loop.start()
    # event loop 실행, 네트워크 호출을 기다리는 동안 프로그램이 다른 일을 수행할 수 있도록 즉시 리턴이 됨

# 콜백 함수의 맨 처음 라인에서 에러를 확인하고 있음을 볼 수 있는데, 이는 콜백에서 예외를 발생시킬 수 없기 때문에 꼭 필요하다
# 콜백에서 어떤 예외라도 발생한다면, 이는 이벤트 루프와 프로그램을 빠져나가므로 모든 에러들은 예외를 일으키는(raise) 대신
# 위처럼 객체로서 전달되어야 한다. 따라서 에러를 처리하는 부분이 없다면, 모든 에러들을 묻혀갈 것임을 의미한다
# 다른 문제점은, 블로킹을 없애는 방법이 유일하게 콜백 뿐이라 매우 긴 콜백 체인을 만들 수 있다는 것이다
# 복잡하며 디버깅이 어렵다는 문제가 있다