from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'
# 평범한 라우팅
# status code 200과 함께 hello 문자열이 날아간다


# 라우팅 함수는 튜플을 리턴할 수 있는데, 이런 방식이다
@app.route('/test')
def test():
    return 'hi', 201
# body, status code 순서

app.run(debug=True)
