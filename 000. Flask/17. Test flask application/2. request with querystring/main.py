from flask import Flask, request

app = Flask(__name__)


# GET 요청의 querystring을 받는 라우팅
@app.route('/', methods=['GET'])
def index():
    return request.args['test_key']


if __name__ == '__main__':
    app.run(debug=True)
