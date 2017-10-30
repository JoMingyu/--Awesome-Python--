from werkzeug.security import safe_str_cmp
# 문자열을 일정한 시간 간격으로 비교한다고 한다
# 되도록이면 ==보다 safe_str_cmp를 활용해 보도록 하자
"""
This function compares strings in somewhat constant time.
This requires that the length of at least one string is known in advance.
Returns `True` if the two strings are equal or `False` if they are not.
"""

if safe_str_cmp('abc', 'abc'):
    print('equal')
