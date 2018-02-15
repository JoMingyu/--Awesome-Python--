# 커스텀 에러도 만들 수 있다
# Java에서 Exception 클래스를 상속받아 구현하듯, 여기서도 Exception 클래스를 상속받자


class CustomError(Exception):
    pass


def raise_error(option):
    if option:
        raise CustomError()
        # 의도적으로 에러를 발생시키기 위해 raise 구문을 사용한다
    else:
        print('normal')

raise_error(False)
try:
    raise_error(True)
except CustomError:
    print('Error!')
