from flask import Flask, request

app = Flask(__name__)


# POST 요청의 body에서 JSON 데이터를 받는 라우팅
@app.route('/', methods=['POST'])
def index():
    return request.json['test_key']


if __name__ == '__main__':
    app.run(debug=True)
