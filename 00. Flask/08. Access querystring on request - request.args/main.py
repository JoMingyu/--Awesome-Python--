from flask import Flask, request

app = Flask(__name__)
# 요청 데이터에 접근할 필요가 있다
# GET에서 자주 사용하는 querystring(ex - localhost:5000/?a=1&b=2)에 접근하도록 하자

# 요청 데이터는 flask 패키지에서 request 객체에 접근해야 한다


@app.route('/')
def index():
    return request.args['test_key']
    # args라는 MultiDict 객체에 접근해서 빼오면 된다
    # MultiDict는 werkzeug.datastructures.TypeConversionDict의 서브클래스인데,
    # 딕셔너리와 거의 동일하게 동작하지만 .get() 메소드에서 type conversion을 지원한다는 장점이 있다

app.run(debug=True)
