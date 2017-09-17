from flask import Flask, request

app = Flask(__name__)
# 요청 데이터에 접근할 필요가 있다
# 특히 GET 메소드로 정의한 리소스에서 사용한다
# flask 모듈에서 request 객체를 가져와야 한다


@app.route('/')
def index():
    return request.args['test_key']
    # args라는 딕셔너리(정확히는 MultiDict)에 접근해서 빼오면 된다

app.run(debug=True)
