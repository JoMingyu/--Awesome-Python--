# Python 3.3까지는 비동기 동시성 프로그래밍을 위한 선택지가 그린 스레드 스타일과 콜백 스타일 뿐이였다
# 더 나은 비동기 프로그래밍을 위해선, 메소드를 부분적으로 실행시키고, 실행을 중단시키고, 스택 객체와 예외를 전역적으로 관리할 수 있는 언어 자체의 지원이 필요하다
# 키워드들만 보면 generator가 힌트가 될 수 있으나, 이의 문제점은 함수가 이를 호출해야만 수행될 수 있다는 것이다
# -> generator는 generator를 호출할 수 없고, 서로의 실행을 중지시킬 수도 없었다
# 이후 PEP 380에서 generator가 다른 generator의 결과값을 yield할 수 있게 해주는 'yield from' 문법이 추가되었다

# https://docs.python.org/3/library/asyncio.html
import asyncio
# 비동기가 정말 generator의 의도는 아니지만, yield from이 추가되며 비동기가 잘 돌아가는 데에 필요한 모든 기능을 제공하게 되었고
# generator를 실행하는 이벤트 루프를 작성한다면, 훌륭한 라이브러리가 될 것이다. 그렇게, asyncio 라이브러리가 탄생했다

# https://github.com/aio-libs/aiohttp
# pip install aiohttp
import aiohttp
# 비동기 네트워크 IO를 위해, aiohttp를 사용하겠다

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

@asyncio.coroutine
def call_url(url):
    print('Starting {}'.format(url))
    session = aiohttp.ClientSession()

    response = yield from session.get(url)
    data = yield from response.text()
    
    print('{} : {}...({} bytes)'.format(url, data[:10], len(data)))
    
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

# 1. 원할 때 객체를 리턴할 수 있고
# 2. 모든 코루틴을 시작한 후 나중에 수집할 수 있고
# 3. 콜백이 없다