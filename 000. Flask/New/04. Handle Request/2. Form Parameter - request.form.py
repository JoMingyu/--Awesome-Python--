from flask import Flask, request

app = Flask(__name__)
# HTTP의 POST 메소드는 보편적으로 서버에게 '리소스를 작성'하라는 의미로 사용. 여기에 얹는 request body의 타입은 요청의 Content-Type 헤더에 따라 결정됨
# request.form은 application/x-www-form-urlencoded, application/form-data 타입의 요청 데이터에 접근한다
# Node.js의 경우 각각 multer, bodyParser를 사용해야 하지만 파이썬은 request.form 하나로 모두 해결 가능하다

@app.route('/', methods=['POST'])
def index():
    return request.form['test_key']
    # form도 args와 동일하게 MultiDict 객체다

if __name__ == '__main__':
    app.run(debug=True)
