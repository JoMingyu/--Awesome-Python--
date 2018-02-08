# pip install flask
from flask import Flask
# 간단한 작업은 간단하게 할 수 있고, 큰 서버도 어렵지 않게 다룰 수 있다
# = Flask는 핵심기능만 간결하게 유지하고, 확장 가능한 것을 목적으로 한다
# https://github.com/pallets/flask
# http://flask-docs-kr.readthedocs.io/ko/latest/

app = Flask(__name__)
# 1. 현재 모듈에 대해 Flask 객체를 생성
# flask.app.Flask - https://github.com/pallets/flask/blob/master/flask/app.py#L67

@app.route('/')
# 2. 데코레이터를 통해 '/'에 라우팅
# flask.app.Flask.route() - https://github.com/pallets/flask/blob/master/flask/app.py#L1186
# 'A decorator that is used to register a view function for a given URL rule'
# 한 endpoint에 대해 할당된 함수를 view function이라고 부른다
def index():
    return 'hello'
    # 문자열 'hello'를 응답으로 전달. status code는 자동 200으로 처리


@app.route('/custom/<int:param>')
# 사용자 정의 URL, 타입은 생략할 수 있으며 기본 타입은 str
def custom(param):
    return param

# 3. 서버 run
# flask.app.Flask.run() - https://github.com/pallets/flask/blob/master/flask/app.py#L822
app.run()
# localhost:5000에서 동작한다
