from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'
# status code 200과 함께 hello 문자열이 날아간다


# 하나의 route와 대응되는 함수를 view function이라고 부른다
# 이 view function은 튜플을 리턴할 수 있고, 각 인덱스의 값이 Flask.Response 클래스에 의해 wrapping된다
@app.route('/test')
def test():
    return 'hi', 201
# body, status code, headers, ...

app.run(debug=True)
