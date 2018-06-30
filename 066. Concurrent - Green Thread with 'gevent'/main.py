# https://github.com/gevent/gevent
# pip install gevent
import gevent
# 동시성 프로그래밍은 Python의 발전과 함께 진화해 왔다
# 멀티 스레딩/프로세싱이 아닌, 비동기 프로그래밍 기반의 동시성을 발전시키고자 많은 움직임들이 있어 왔다

# gevent는 비동기 프로그래밍의 가장 기초인 그린 스레드(어플리케이션 레벨에서 관리되는 스레드)를 제공
# gevent의 API는 스레딩과 유사해 보이지만, 실제 구현을 보면
# C 확장 모듈 형태로 제공되는 경량 코루틴인 Greenlet을 사용하여, 코루틴들을 이벤트 루프 위에서 실행한다
from urllib.request import urlopen

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def print_head(url):
    print('Starting {}'.format(url))
    
    data = urlopen(url).read()
    print('{} : {}...({} bytes)'.format(url, data[:10], len(data)))

jobs = [gevent.spawn(print_head, _url) for _url in urls]

gevent.wait(jobs)
# 이는 코루틴에 대한 이해 없이도 경량 스레딩을 통한 비동기 프로그래밍이 가능하다는 이점이 있음을 의미하나,
# context switching을 제외하면 스레딩이 가져오는 다른 문제점들을 가지고 있다