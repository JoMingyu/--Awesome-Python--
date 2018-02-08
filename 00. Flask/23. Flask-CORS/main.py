from flask import Flask
# pip install flask-cors

from flask_cors import CORS
# Cross-Origin Resource Sharing(CORS)을 지원하기 위한 패키지
# app 객체의 데코레이터(after_request)를 활용해도 되는데, 이 패키지를 사용하면 한 줄로 CORS 헤더 세팅이 가능해서 편하다
# Flask-CORS도 내부적으로는 app 객체의 after_request 데코레이터를 이용한다
# https://github.com/corydolphin/flask-cors/blob/master/flask_cors/extension.py#L153

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
