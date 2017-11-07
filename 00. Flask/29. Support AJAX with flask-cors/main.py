from flask import Flask
from flask_cors import CORS
# AJAX를 지원하기 위해 flask-cors를 사용하면 된다
# app 객체의 데코레이터를 활용해도 되는데, 이 패키지를 사용하면 한 줄로 CORS 헤더 세팅이 가능해서 편하다

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
