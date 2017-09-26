from flask import Flask
# 커스텀 HTTPException을 만들어 보자
# 여기선 Flask의 abort()를 사용하지 않는다

from werkzeug.exceptions import HTTPException, default_exceptions, Aborter
# werkzeug 패키지의 exceptions 모듈로부터 HTTPException 클래스, default_exceptions 리스트, Aborter 클래스를 받아온다

from werkzeug.http import HTTP_STATUS_CODES
# werkzeug 패키지의 http 모듈로부터 HTTP_STATUS_CODES 리스트를 받아온다
# 이걸 가져오는 이유는 아래에서 다시 설명한다


class Payme(HTTPException):
    # HTTPException 클래스를 상속받아 클래스를 하나 만든다

    code = 777
    # code 필드는 필수

    description = 'Hello?'
    # description 필드는 옵션이다. Status message에 보내지는 건줄 알았는데, <p> 태그에 들어가는 설명이었다.

default_exceptions[777] = Payme
# 기본 exception에 내가 만든 오류 코드를 심는다

abort = Aborter()
# abort는 werkzeug.exceptions 모듈에서 가져온 Aborter의 객체이다

HTTP_STATUS_CODES[777] = 'Hello'
# 이건 없어도 되지만, status message를 관리하기 위해 사용한다
# werkzeug.http 모듈의 HTTP_STATUS_CODE는 status code와 message로 이루어진 딕셔너리다

app = Flask(__name__)


@app.route('/')
def index():
    abort(777)

app.run(debug=True)
