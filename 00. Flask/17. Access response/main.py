# -- 알아볼 부분
# flask.helpersmake_response() - https://github.com/pallets/flask/blob/master/flask/helpers.py#L152
# flask.wrappers.Response - https://github.com/pallets/flask/blob/master/flask/wrappers.py#L177
# werkzeug.wrappers.BaseResponse - https://github.com/pallets/werkzeug/blob/master/werkzeug/wrappers.py#L718

from flask import Flask
from flask import make_response
from flask import Response
# make_response() 함수 또는 Response 클래스를 통해 response 객체를 만들 수 있다

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('Body data', 200)
    # 1. flask.helpers.make_response 함수를 이용한 방법
    # 들어가는 argument가 없다면 Response 클래스를 사용하고, 외의 경우 Flask 인스턴스의 make_response 메소드를 사용
    # https://github.com/pallets/flask/blob/master/flask/app.py#L1847

    # 헤더를 설정해 보자
    response.headers['Something'] = 'Value'
    # werkzeug.datastructures.Headers 클래스의 인스턴스

    return response


@app.route('/2')
def index2():
    response = Response('Hello', 200)
    # 2. flask.wrappers.Response 클래스를 이용한 방법

    return response

app.run(debug=True)
