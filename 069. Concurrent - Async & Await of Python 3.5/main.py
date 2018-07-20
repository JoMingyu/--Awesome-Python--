# asyncio는 많은 지지를 얻었고, Python 3.5에서는 이를 표준 라이브러리로 만들었으며, async와 await 키워드가 추가되었다
# async, await은 asyncio의 API를 이용한 비동기 코루틴을 사용하기 위한 문법이다
# async는 코루틴으로 정의하려는 함수의 'def' 앞에 붙이며, 'await'은 코루틴 내에서 다른 코루틴을 호출하고 그 결과를 받을 때 사용한다
# 각각 @asyncio.coroutine 데코레이터, 'yield from' 키워드를 대체한다

import asyncio
import aiohttp

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def call_url(url):
    print('Starting {}'.format(url))

    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.text()

        print('{} : {}...({} bytes)'.format(url, data[:10], len(data)))

        return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
# 이제 완벽한 단일 스레드 기반의 non-blocking 비동기 코루틴이 완성되었다. 요약해 보자

"""
1. Python 3.3까지 비동기 프로그래밍을 위한 선택지는 두 가지가 있었다
    (1) 그린 스레드 스타일(gevent 등..)
        - 스레드들이 하드웨어 대신 어플리케이션 레벨에서 관리됨
        - 일반 스레드와 유사해서, 코루틴에 대한 이해가 부족하더라도 스레드만 이해하고 있다면 사용하기 좋음
        - CPU 컨텍스트 스위칭 문제를 제외한 일반 스레드 프로그래밍이 가진 모든 문제점들을 가지고 있음(기아, 경쟁 상태, ...)
    (2) 콜백 스타일(tornado 등..)
        - 콜백은 예외를 발생시키지 않음
        - 콜백은 수집할 수 없음
        - 콜백의 콜백은 복잡하며 디버깅이 어려움

2. Python 3.4부터 generator로 비동기 코루틴을 구현할 수 있게 됐다
    - generator가 다른 generator의 결과값을 yield할 수 있게 해주는 'yield from' 문법이 추가되었다
    - 이를 통해 비동기 코루틴을 만들 수 있게 되었고, 이들을 실행하는 이벤트 루프 라이브러리로서 asyncio가 탄생했다

3. Python 3.5에서 생긴 async/await
    - asyncio 라이브러리가 많은 지지를 얻어 파이썬 표준 라이브러리가 되었고
    - 비동기 표현식을 위한 async, yield from을 대체하는 await 키워드가 추가되었다

4. asyncio라는 훌륭한 비동기 프레임워크는 스레딩의 문제점들을 명쾌하게 해결한다
    - 컨텍스트 스위칭
        asyncio는 비동기이며 이벤트 루프를 사용하기에, I/O를 대기하는 동안
        어플리케이션이 컨텍스트 관리할 수 있도록 한다. CPU 스위칭이 사라진다.
    - 경쟁 조건
        asyncio는 한 번에 하나의 코루틴만 실행하며 정의된 지점에서만 스위칭이 일어나기에, 경쟁 조건으로부터 안전하다
    - 데드락, 라이브락
        경쟁 조건에 대해 걱정할 필요가 없기 때문에 잠금을 사용할 필요가 없으며, 이는 데드락으로부터 매우 안전한 환경을 만들어 준다
        두 개의 코루틴이 서로를 깨워야 할 필요가 있을 경우엔 데드락의 가능성이 있지만, 이런 일은 매우 드물 것이다

5. 비동기 프로그래밍을 위한 옵션들이 많지만, 현재까진 asyncio가 최고다. 다음 프로젝트에서는 병렬 처리를 위해 asyncio를 써보자.
"""