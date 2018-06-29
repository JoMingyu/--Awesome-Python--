# https://github.com/gevent/gevent
# pip install gevent
import gevent
# gevent는 비동기 프로그래밍의 가장 기초인 그린 스레드(Green Thread)를 제공
# 스케줄링을 하드웨어가 아닌 어플리케이션 레벨에서 대신 한다는 점을 제외하면, 일반 스레드와 매우 유사해 보인다
from urllib.request import urlopen

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def print_head(url):
    print('Starting {}'.format(url))
    
    data = urlopen(url).read()
    print('{} : {}...({} bytes)'.format(url, data[:10], len(data)))

jobs = [gevent.spawn(print_head, _url) for _url in urls]

gevent.wait(jobs)
# gevent의 API는 스레딩과 유사해 보이지만, 실제 구현을 보면 스레드 대신 코루틴을 사용하며
# 스케줄링을 위해 코루틴들을 이벤트 루프 위에서 실행한다
# 이는 코루틴에 대한 이해 없이도 경량 스레딩의 이점을 얻을 수 있음을 의미하나,
# context switching을 제외하면 스레딩이 가져오는 다른 문제점들을 가지고 있다