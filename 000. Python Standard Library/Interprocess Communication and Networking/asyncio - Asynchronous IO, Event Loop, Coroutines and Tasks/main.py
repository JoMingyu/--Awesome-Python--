# https://docs.python.org/3/library/asyncio.html
import asyncio
# https://github.com/python/cpython/tree/3.6/Lib/asyncio/
# asyncio는 Python 3.4에서 새로 추가되었다. 코루틴을 사용하여 단일 스레드 concurrent 코드를 작성하고
# Node.js의 event-driven과 동일한 Non-blocking I/O와 같은 형태의 비동기 IO를 통해 조금 더 효율적으로 동시에 코드를 돌릴 수 있게 해준다
# CPU에 부하가 집중되는 다른 작업들과는 달리 I/O 작업은 CPU와 개별적으로 동작이 가능하다는 점에 착안하여, I/O 처리를 기다리는 역할을 코루틴에게 위임하고
# 그 시간동안 다른 코루틴을 이용해서 별도의 작업을 또 비동기로 처리할 수 있다

# 여기서 말하는 코루틴은 generator를 이용해 메인 루틴과 흐름을 분리하여 동작하는(yield에 값을 send하는, 동기 코루틴) 기존의 코루틴과는 완전히 구분할 필요가 있다
# 동작하는 방식 자체로는 코루틴이라는 표현은 정확하나, 일반적으로 사용하던 generator coroutine과는 다른 관점에서 봐야 하는, 비동기 형태의 코루틴이다

@asyncio.coroutine
# 비동기로 호출되는 코루틴 함수를 정의하기 위해 사용하는 데코레이터
def greet(msg):
    yield from asyncio.sleep(1)
    # yield from : asyncio.coroutine이 붙은 함수에서만 사용 가능한 표현으로, 다른 비동기 코루틴을 호출하되, 해당 작업이 완료될 때까지 기다린다는 의미
    print(msg)

# 이는 time.sleep()을 이용해서 1초 지연한 후 메시지를 출력하는 코드와 아무런 차이가 없으나,
# time.sleep(1)은 현재 스레드를 1초 동안 정지시키지만, 비동기 코루틴 스레드를 중지시키지 않는다

# @asyncio.coroutine 데코레이터를 붙여 정의한 함수는 코루틴을 생성해주는 함수가 된다. 즉 위의 함수들을 실행하면 1초 후에 메시지가 출력되는 것이 아니라, 아무 일도 일어나지 않는다
greet('Hello')

# 이를 실제로 실행하기 위해서는 asyncio.ensure_future()를 이용한다(Python 3.4에서는 asyncio.asnyc())
# 해당 함수는 코루틴 객체(코루틴 생성함수를 실행하여 리턴된 객체)를 인자로 받아 Task 객체를 반환해 주는데,
# Task는 Future의 서브 클래스이며, concurrent.futures에 정의된 Future 클래스와 거의 동일한 API를 제공(런루프에 의해 스케줄링된 Future를 제공)한다
loop = asyncio.get_event_loop()
loop.run_until_complete(greet('Hello'))

# * @asyncio.coroutine과 yield from은 Python 3.5 이상에서 각각 async def와 await 키워드로 대체 가능하다
