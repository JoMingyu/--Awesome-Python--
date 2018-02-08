# 패키지를 이용하면 모듈을 계층적으로 관리할 수 있게 된다
# 패키지 내의 모듈은 패키지.모듈 : A.B 형식으로 관리된다. 자료구조의 Tree로 생각하면 편하다

# 패키지 내의 모듈 import는 이렇게
import some_package.another_module
# 도트 연산을 하면 된다
some_package.another_module.say_hello()

# 접근이 너무 기니까 from ~ import를 사용해 보자
from some_package import another_module
another_module.say_hello()

# 패키지 내의 모든 모듈 import
from some_package import *
# 패키지 내의 모든 모듈을 import한다고 쳤을 때(from 패키지 import 모듈)
# __init__.py에 __all__ 변수가 설정되어 있지 않으면 모듈 접근 시 NameError가 발생한다.
another_module2.say_hello()
# __init__.py의 내용을 확인해 보도록 하자

# 패키지 내 모듈의 함수만 import한다면
from some_package.another_module import say_hello
say_hello()

# 와일드카드 import도 물론 가능
from some_package.another_module import *
say_hello()
say_hi()

# 모듈과 패키지에서 중요한 건
# 1. __init__.py의 __all__ 변수
# 2. 상황에 따른 import(모듈 import, 또는 모듈 내 요소 import)
