# -- 알아볼 부분
# flask.app.Flask.errorhandler() - https://github.com/pallets/flask/blob/master/flask/app.py#L1248

from flask import Flask, abort

app = Flask(__name__)


@app.errorhandler(404)
# 서버에서 HTTP 예외 코드(400번대 이상)가 리턴되는 경우 해당 리턴의 response를 직접 핸들링할 수 있다
# ex) 모든 404 not found에 대하여 커스텀 404 페이지 리턴 등
# https://github.com/adsfokow 를 보면 알거다
def error(e):
    # 클라이언트가 404를 얻어갔다면 이쪽으로 온다
    print(type(e))
    print(e)
    # e는 에러 코드와 에러 메시지를 그대로 가지고 있다
    return 'hello'


@app.route('/')
def test():
    abort(404)

app.run(debug=True)
