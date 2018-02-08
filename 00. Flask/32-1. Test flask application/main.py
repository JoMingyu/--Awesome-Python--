# -- 알아볼 부분
# flask.app.Flask.test_client() - https://github.com/pallets/flask/blob/master/flask/app.py#L929
# flask.testing.FlaskClient - https://github.com/pallets/flask/blob/master/flask/testing.py#L69
# werkzeug.test.Client - https://github.com/pallets/werkzeug/blob/master/werkzeug/test.py#L652

# 내 Flask 앱 테스팅을 위한 간단한 서버를 만들자
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
