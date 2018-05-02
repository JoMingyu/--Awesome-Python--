# Doctsring은 따옴표(보통 큰따옴표) 3개로 이루어진 문자열로 정의하는 주석의 일종
# '#' 기호를 사용하는 주석은 런타임에 제거되지만, docstring은 제거되지 않고 하나의 속성으로서 분류됨
def sum(a, b):
    """
    Returns a + b

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: a + b
    """
    # docstring의 스타일은 여러가지가 있으나, 대포적으로 위와 같은 Google Style을 사용한다
    # http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    return a + b

print(sum.__doc__)
# 
#   Returns a + b
#
#   Args:
#       a (int): first number
#       b (int): second number
#
#   Returns:
#       int: a + b
#
