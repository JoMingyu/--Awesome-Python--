# 코드 재사용을 위해서 모듈화는 참 중요하다
# 여기도 'main'이라는 이름을 가진 모듈이다(main.py)

# another_module을 불러오려면 import를 쓰면 된다
import another_module
another_module.say_hello()

# from ~ import를 이용하면 특정 함수나 클래스만 직접 import할 수 있다
from another_module import say_hello
say_hello()

# 와일드카드 import가 가능하다
from another_module import *
# another_module 내의 모든 것을 import한다
say_hello()
say_hi()

# PEP8 표준의 import는

# 항상 파일의 맨 위에 import문을 놓는다
# 모듈을 import할 때는 항상 모듈의 절대 이름을 사용하며 현재 모듈을 기준으로 한 상대 경로를 사용하지 않는다
# 상대적인 import를 해야 한다면 명시적인 구문을 써서 from . import another_module이라고 한다
# import는 표준 라이브러리 모듈, 서드파티 모듈, 자신이 만든 모듈 순으로 구분해야 한다
