from flask import Flask, request

app = Flask(__name__)


# POST의 body data를 받는 간단한 라우팅
@app.route('/', methods=['POST'])
def index():
    return request.form['test_key']


if __name__ == '__main__':
    app.run(debug=True)
