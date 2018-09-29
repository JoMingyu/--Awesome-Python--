# imported name에 별명(alias)을 붙여줄 수 있다
# import - as / from - import - as를 사용한다

import calculator as calc
print(calc.calculate(calc.add, 1, 3)) # 4

from calculator import calculate as calc, add as a
print(calc(a, 1, 3)) # 4
