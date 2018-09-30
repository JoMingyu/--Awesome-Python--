# 해당 모듈은 패키지 자체(여기서는 calculators)에 대한 namespace가 되며,
# 패키지의 특정 요소를 import하는 경우, 패키지의 __init__.py가 먼저 import된다
# 초기화 구문이나, 아래와 같은 import 중계를 위한 용도로 사용된다

from calculators.operator import calculate