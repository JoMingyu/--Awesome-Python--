"""
Without arguments, return the list of names in the current local scope.
With an argument, attempt to return a list of valid attributes for that object.
"""

# dir 함수는 인자로 들어온 객체의 네임 스페이스에 있는 유효한 애트리뷰트의 네임목록 을 반환한다.
# 만약, 인자를 주지 않을 경우에는 현재 로컬 범위에 있는 모든 애트리뷰트의 네임을 반환한다.

import os

# os 가 가지고 있는 유효한 애트리뷰트의 네임 목록을 반환한다.
print(dir(os))


# 매직메서드 __dir__() 이 정의되어있으면 dir()은 __dir__() 의 리턴값을 반환한다.
class Python:
    def __dir__(self):
        return ['Interpreter', 'Dynamically Typed', 'Iteractive language']


lang = Python()
print(dir(lang))

# 인자가 없을 경우 (1)
print(dir())


# 인자가 없을 경우 (2)
def test_dir():
    a = 1
    print(dir())


test_dir()
