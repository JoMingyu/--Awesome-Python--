# 코드 재사용을 위해서 모듈화는 참 중요하다
# 여기도 main 모듈이다

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
