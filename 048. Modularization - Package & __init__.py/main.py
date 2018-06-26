# 패키지는 비슷한 성격을 가진 모듈들을 모아 분류하고, 관리하기 위해 사용한다
# 모듈을 가져와 사용할 때처럼, 여기서도 import / from - import 구문을 사용한다
import calculators
# calculators 패키지(__init__.py) import

from calculators.functions.basic import *
from calculators.functions.custom import *
# calculators.functions.basic과 .custom의 모든 요소 import

print(calculators.calculate(add, 1, 3))
# 4

print(calculators.calculate(is_divisor, 5, 3))
# False