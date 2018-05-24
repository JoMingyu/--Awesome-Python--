# async, await은 asyncio를 이용한 비동기 코루틴을 위해 Python 3.5에서 새로 추가된 문법이다. 따라서 asyncio의 API를 위한 문법이며, generator를 이용한 코루틴은 이 문법을 적용하지 않는다
# async는 코루틴으로 정의하려는 함수의 'def' 앞에 붙이며, 'await'은 코루틴 내에서 다른 코루틴을 호출하고 그 결과를 받을 때 사용한다
# 각각 @asyncio.coroutine 데코레이터, 'yield from' 키워드를 대체한다

import asyncio

# 아래의 함수는 1초동안 대기한 후 메시지를 출력한다
async def greet(msg):
    await asyncio.sleep(1)
    print(msg)

# Python 3.4에서는 다음과 같이 사용한다
@asyncio.coroutine
def greet(msg):
    yield from asyncio.sleep(1)
    print(msg)

loop = asyncio.get_event_loop()
loop.run_until_complete(greet('Hello'))
