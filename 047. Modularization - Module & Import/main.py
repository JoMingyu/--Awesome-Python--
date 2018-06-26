# 모듈은 비슷한 기능을 하는 함수나 클래스들을 묶어 재사용성을 높이기 위해 사용된다
# calculator.py 모듈을 생성하여 계산에 관한 함수들을 정의해 두었으며, 이들은 아래처럼 import 구문을 통해 가져와 사용할 수 있다
import calculator
print(calculator.calculate(calculator.add, 1, 3))
# 4
# calculator의 요소들은 calculator.[...] 형태로 접근해야 한다

# 아래와 같은 from - import 구문을 통해 해당 모듈의 특정 요소들만 가져올 수도 있으며
# 여러 개를 한 번에 import할 경우 요소들을 콤마로 구분하여 명시하면 된다
from calculator import calculate, add
print(calculate(add, 1, 3))
# 4

# 모든 요소를 import하기 위해 와일드카드 표현식인 asterisk(*)를 사용할 수 있다
from calculator import *
print(calculate(sub, 3, 1))
# 2

# 상대 경로 import도 가능하다
from .calculator import *
# 일반적인 경우 이와 같은 상대 경로 사용은 bad practice로 분류되며, 보통 라이브러리 개발 시 사용된다