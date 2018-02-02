from flask import Flask, request

app = Flask(__name__)
# POST에서 자주 사용하는 multipart/form-data와 application/x-www-form-urlencoded에 접근하자
# 옆동네 Node.js의 경우 각각 multer, bodyParser를 사용해야 하지만 파이썬은 request 객체면 다 끝난다


@app.route('/', methods=['POST'])
def index():
    return request.form['test_key']
    # form도 args와 동일하게 MultiDict 객체다

app.run(debug=True)
