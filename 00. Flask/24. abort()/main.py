# -- 알아볼 부분
# flask.abort() - https://github.com/pallets/flask/blob/master/flask/__init__.py#L17
# werkzeug.exceptions.abort() - https://github.com/pallets/werkzeug/blob/master/werkzeug/exceptions.py#L690

from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    abort(400)
    # abort() 함수는 HTTP 예외 코드(400번대 이상의 상태 코드)를 리턴해주는 역할을 한다

    # abort를 flask 패키지에서 가져왔는데, flask/__init__.py를 보면 알 수 있듯
    # werkzeug.exceptions 모듈에서 abort 함수를 중계해주는 역할일 뿐이다
    # 따라서 'from flask import abort'와 'from werkzeug.exceptions import abort'는 동일한 구문

app.run(debug=True)
