from flask import Flask, request

app = Flask(__name__)
# HTTP의 POST 메소드는 데이터를 서버로 보내는 방법 중 하나. request body의 타입은 Content-Type 헤더에 따라 결정됨
# request.form은 application/x-www-form-urlencoded와 application/form-data 타입에 대응된다
# 옆동네 Node.js의 경우 각각 multer, bodyParser를 사용해야 하지만 파이썬은 request 객체면 다 끝난다


@app.route('/', methods=['POST'])
def index():
    return request.form['test_key']
    # form도 args와 동일하게 MultiDict 객체다

app.run(debug=True)
