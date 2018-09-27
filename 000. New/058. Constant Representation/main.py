# Python에는 타 언어에서 상수를 표현하는 const나 final같은 키워드가 없다
# Python에서 상수는 대문자로만 구성된 이름을 사용하여 표현하는 관례가 있다. private을 _name처럼 표현했던 것처럼 말이다

CONST_NAME = True
DESCRIBES_TEN = 10
# 이것도 private과 동일하게, 진정한 의미의 상수는 아니며 '변경 불가능함'을 권고하는 용도로 사용된다
