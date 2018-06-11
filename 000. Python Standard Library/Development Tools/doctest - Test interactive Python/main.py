# https://docs.python.org/3/library/doctest.html
import doctest
# https://github.com/python/cpython/blob/3.6/Lib/doctest.py
# 함수의 docstring에 파이썬 세션 형태의 함수 호출 시나리오를 적어 두고 doctest를 돌리면
# 해당 docstring과 결과가 일치하는지를 체크한다

def fun(x):
    """
    >>> fun(3)
    4
    >>> fun(-1)
    0
    """
    return x + 1

if __name__ == '__main__':
    doctest.testmod()
    # 테스트에 성공하면 콘솔에 아무 것도 출력되지 않고, 실패하면 어느 부분에서 실패했는지를 콘솔에 출력한다
