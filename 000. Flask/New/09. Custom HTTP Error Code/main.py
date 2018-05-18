from flask import Flask, abort
# 커스텀 HTTPException을 만들어 보자

from werkzeug.exceptions import HTTPException, default_exceptions, Aborter, _aborter
from werkzeug.http import HTTP_STATUS_CODES


class Payme(HTTPException):
    # werkzeug.exceptions.HTTPException 클래스를 상속받아 클래스를 하나 만든다

    code = 777
    # code 필드는 필수

    description = 'Hello?'
    # description 필드는 옵션이다. Status message에 보내지는 게 아니라, <p> 태그에 들어가는 설명이다

default_exceptions[777] = Payme
# 기본 exception에 직접 만든 오류 코드를 심는다

# werkzeug.exceptions.abort()는 내부적으로 _aborter 객체를 호출(__call__())한다
# > return _aborter(status, *args, **kwargs)

# 해당 _aborter 객체는 아래처럼 초기화된다
# > _aborter = Aborter()
# 따라서 werkzeug.exceptions._aborter 객체를 다시 초기화해 주어야 한다
_aborter = Aborter()

HTTP_STATUS_CODES[777] = 'Hello'
# 이건 없어도 되지만, status message를 관리하기 위해 사용한다
# werkzeug.http.HTTP_STATUS_CODE는 status code와 message로 이루어진 딕셔너리다

app = Flask(__name__)


@app.route('/')
def index():
    abort(777)

if __name__ == '__main__':
    app.run(debug=True)
