# https://docs.python.org/3/library/enum.html
import enum
# https://github.com/python/cpython/tree/3.6/Lib/enum.py
# enumeration은 고유하고 상수에 바인딩된 symbolic name의 집합
# enum 모듈은 고유한 값의 set들을 정의하기 위한 Enum, IntEnum, Flag, IntFlag 클래스를 제공한다

class Nickname(enum.Enum):
    GENI429 = '정근철'
    PLANB = '조민규'
    FLOUIE = '정경서'

print(Nickname.PLANB)
# Nickname.PLANB

print(isinstance(Nickname.PLANB, Nickname))
# True
# enum의 멤버 타입은 해당 enum 클래스와 같음

print(repr(Nickname.PLANB))
# <Nickname.PLANB: '조민규'>
# __repr__()에 더 많은 정보가 담겨 있음

print(Nickname.PLANB.name)
# 'PLANB'

print(Nickname.PLANB.value)
# '조민규'

# --- 프로그래밍적인 접근

for nickname in Nickname:
    # enum은 iteration을 지원
    print(nickname)

# Nickname.GENI429
# Nickname.PLANB
# Nickname.FLOUIE

print(Nickname('조민규'))
# Nickname.PLANB

print(Nickname['PLANB'])
# Nickname.PLANB

print(list(Nickname))
# [<Nickname.GENI429: '정근철'>, <Nickname.PLANB: '조민규'>, <Nickname.FLOUIE: '정경서'>]

@enum.unique
class Mistake(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 3
    # ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE 발생