from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    # 자동으로 '200 OK'로 처리되는 status code를 명시적으로 변경할 수 있다
    return 'hello', 204
    # 위처럼 view function은 튜플을 리턴할 수 있고,
    # 내부적으로 각 인덱스의 값이 wrappers.Response의 생성자에 전달되어 객체가 생성된다
