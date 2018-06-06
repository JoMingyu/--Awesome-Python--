# https://docs.python.org/3/library/builtins.html
import builtins
# 파이썬의 모든 빌트인에 직접 접근할 수 있다
# 예를 들어, builtins.open()은 빌트인 함수 open()의 full name이다

# 일반적으로 builtins.*** 형태로 명시적으로 액세스하지 않지만 빌트인과 같은 이름의 wrapper 함수를 만드는 등의 일을 할 때 유용하다
class UpperCaser:
    def __init__(self, f):
        self._f = f
    
    def read(self, count=-1):
        return self._f.read(count).upper()

def open(path):
    f = builtins.open(path, 'r')
    return UpperCaser(f)
