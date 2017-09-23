# 내 Flask 앱 테스팅을 위한 간단한 서버를 만들자
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
