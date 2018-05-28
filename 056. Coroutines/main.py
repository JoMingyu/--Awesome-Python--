# Generator가 데이터의 생산자라면, Coroutines은 데이터의 소비자
# 코루틴은 '진입점이 여러 개인 함수'를 의미하며, Python은 이 '진입점'을 yield로 표현함
# Python 2.5에서 yield는 표현식이 됨(이전까지는 값을 내놓은 지점을 설정하는 용도였으나, 표현식이 됨으로써 값으로 평가됨)
# 이를 통해 외부에서 generator로 값을 주입할 수 있게 됨

def finder(str_for_find):
    while True:
        s = (yield)
        if str_for_find in s:
            print('Found : {} in {}'.format(str_for_find, s))
            
f = finder('coroutine')
# 생성 직후 코루틴의 실행 직후는 while True 이전에 멈춰 있음

next(f)
# s = (yield) 구문을 만나 멈추게 됨
# 해당 표현식은 단순한 바인딩 구문이며, 우변인 yield가 평가되기 이전까지 코루틴이 멈춰 있음
# Generator로 생성된 객체는 __next__()와 send() 메소드를 가지는데,
# 전자는 다음번 yield 구문을 실행하기 위한 메소드이며, 후자는 코루틴 내부의 yield로 값을 밀어넣는 역할을 함

f.send('PlanB')
f.send('This is coroutine')
# Found : "coroutine" in "This is coroutine"
# Generator를 사용한 코루틴은 generator coroutine이라고도 부른다