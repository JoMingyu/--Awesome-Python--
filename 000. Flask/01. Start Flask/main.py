# 가벼운 웹서버 프레임워크 flask
# pip install flask
from flask import Flask
# 간단한 작업은 간단하게 할 수 있고, 큰 서버도 어렵지 않게 다룰 수 있다
# 지원하는 것들이 많은 만큼 알고 있어야 하는 문법적 요소들이 꽤 있다

app = Flask(__name__)
# 현재 모듈에 대해 Flask 객체를 생성


@app.route('/')
# 데코레이터를 통해 '/'에 라우팅
def index():
    return 'hello'
    # 문자열 'hello'를 응답으로 전달. status code는 자동 200으로 처리


@app.route('/custom/<param>')
# 사용자 정의 URL
def custom(param):
    return param


app.run()
# 기본 포트는 5000
