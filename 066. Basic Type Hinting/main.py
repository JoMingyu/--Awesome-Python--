# 동적 타입 검사는 파이썬의 주요 selling point였고, 원래 이 점에 대해 별다른 변경 계획이 없었다가
# 1. PEP 3107에 의해 Python 3.0에서 Function Annotation이 만들어졌다
def compile(source: "something compilable",
            filename: "where the compilable thing comes from",
            mode: str):
    ...
# 처음에는 인자에 설명을 적어두는 용도였지만, 빌트인 타입도 써놓을 수 있게 되면서 어느 정도의 type hinting이 시작되었다

# 2. 귀도 반 로썸의 PEP 484에 의해 Python 3.5에서 수많은 형태의 type hint들이 만들어졌다
def greeting(name: str) -> str:
    return 'Hello {}'.format(name)

# 3. PEP 526에 의해 Python 3.6에서 Variable Annotation이 만들어졌다
primes: list = []
captain: str
# PEP 484가 함수 단위에서의 type hinting에 집중했다면, PEP 526은 변수에 대한 적용에 집중했다

# 파이썬은 타입이 확정되는 시기가 런타임이라, IDE 레벨에서의 자동완성 지원이 참 껄끄러웠는데 type hinting이 이걸 해결해 주었다
# 그러나 귀도의 PEP 484에서 제시한 type hinting은 말 그대로 'hint'를 위한 것이라, 동적 타입 검사가 그대로 유지된다
# 따라서 mismatched type을 전달해도 상관이 없다(= 타입이 안맞아서 TypeError를 raise한다거나 하는 불평을 하지 않는다)
print(greeting(123)) # Hello 123
# 정적 타입 검사를 하려면 mypy같은 외부 툴을 사용하거나, PyCharm을 사용하면 된다
# 물론 이것도 파이썬이 정적 검사를 하도록 하는 플러그인 같은 게 아니라 그냥 '검사' 용도라는 것을 잘 알고 넘어가자

# type hinting은 타입 검사 타임에 신경쓰지 말고, 딱 주석의 역할 정도로 사용하는 것이 좋다
# 그래도 타입에 대한 정보를 명시할 수 있다는 것은 정말 좋은 일
# 그런데 '문자열로 이루어진 리스트', 'int나 float 타입 중에 하나' 'Iterable 타입'같은 것을 표현하려면 typing 모듈이 필요하다
# -> 궁금하다면 101번 챕터로 이동

# - 번외
# 그 이전에도 type comments라는 개념으로, 파이썬 유저들 사이에서 아래같은 야매 타이핑이 좀 쓰이긴 했다
def split_str(source, seperator=' '):
    # type: (str, str) -> list

    return source.split(seperator)

# mypy는 이런 형태의 타이핑도 지원하고 있기 때문에
# Python 2같은 환경에서 type hinting을 쓰고 싶다면 도움될 수 있으니 따로 알아보면 되겠다
# 어차피 Python 3.5+ 사용자라면 공식 지원 덕에 syntax로서 지원받을 수 있으니 옛날 얘기 듣듯이 넘어가자
