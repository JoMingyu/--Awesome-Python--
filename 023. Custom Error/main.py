# 커스텀 에러도 만들 수 있다
# Exception 클래스를 상속받자


class CustomError(Exception):
    pass


def raise_error(option):
    if option:
        raise CustomError()
    else:
        print('normal')

raise_error(False)
try:
    raise_error(True)
except CustomError:
    print('Error!')
