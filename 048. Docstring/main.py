# 3개의 따옴표로 감싸진 문자열을 함수나 클래스 정의문의 최상단에 붙이면, 의미 없는 statement가 아닌 'docstring'이라는 것으로 분류된다
# '#' 기호를 사용하는 주석은 런타임에 제거되지만, docstring은 제거되지 않고 함수나 클래스의 속성으로서 관리할 수 있다

def sum(a, b):
    """
    Returns a + b

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: a + b
    """
    # docstring의 스타일은 여러가지가 있으나, 대표적으로 위와 같은 Google Style을 사용한다
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

print(help(sum))
# Help on function sum in module __main__:
#
# sum(a, b)
#     Returns a + b
#
#     Args:
#         a (int): first number
#         b (int): second number
#
#     Returns:
#         int: a + b

# 위처럼 함수의 __doc__ 속성이나, 빌트인 함수 help에 전달하여 docstring을 볼 수 있다
# 파이썬의 여러 빌트인 함수들도 docstring을 가지고 있다
print(help(len))
# Help on built-in function len in module builtins:
#
# len(obj, /)
#     Return the number of items in a container.

# 라이브러리 문서화에 용이하게 사용되고, docstring을 기반으로 한 테스트 프레임워크(doctest)도 존재한다
