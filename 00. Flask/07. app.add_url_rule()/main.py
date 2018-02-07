# -- 알아볼 부분
# flask.app.Flask.add_url_rule() - https://github.com/pallets/flask/blob/master/flask/app.py#L1212

from flask import Flask

app = Flask(__name__)


# 데코레이터 없이 함수를 선언하고
def index():
    return 'hello'

app.add_url_rule('/index', 'endpoint!!', index)
# Flask 객체의 add_url_rule이라는 메소드로 리소스를 추가한다
# rule, endpoint, view_func 순서
# route 데코레이터 안에서도 self.add_url_rule로 엔드포인트에 view function을 할당한다

app.run()
