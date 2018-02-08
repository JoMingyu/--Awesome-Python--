from flask import Flask, request

app = Flask(__name__)


# POST 요청의 form-data 또는 urlencoded 데이터를 받는 라우팅
@app.route('/', methods=['POST'])
def index():
    return request.form['test_key']


if __name__ == '__main__':
    app.run(debug=True)
