from flask import Flask, abort

app = Flask(__name__)


@app.errorhandler(404)
# 오류에 해당하는 status code에 대해 핸들러를 만들어 준다
# ex) 모든 404 not found에 대하여 예쁜 페이지 처리
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
