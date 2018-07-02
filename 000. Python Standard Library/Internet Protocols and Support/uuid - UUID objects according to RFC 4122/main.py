# https://docs.python.org/3/library/uuid.html
import uuid
# https://github.com/python/cpython/blob/3.6/Lib/uuid.py
# RFC 4122 표준의 UUID 버전 1, 3, 4, 5를 지원하는 UUID generator 라이브러리

print(uuid.uuid1())
# UUID('...')
# MAC 주소와 현재 시간을 nanosecond로 환산하고 이를 조합

print(uuid.uuid3())
# UUID('...')
# MD5 해시 사용

print(uuid.uuid4())
# UUID('...')
# 철저히 무작위, 또는 의사 난수(pseudo-random)에서 UUID 생성. 보장된 고유 번호를 제공하진 않으나, 중복 가능성은 매우 낮음

print(uuid.uuid5())
# UUID('...')
# SHA-1 해시 사용