# Python 빌트인 클래스인 Exception을 상속받아 사용자 정의 에러를 만들 수 있다
class CustomError(Exception):
    pass


def raise_error():
    raise CustomError('This is Error!')
    # 에러를 발생시키기 위해 raise statement를 사용한다


try:
    raise_error()
except CustomError as e:
    print(e.args)
