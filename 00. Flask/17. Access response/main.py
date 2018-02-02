from flask import Flask, make_response, Response
# make_response() 함수 또는 Response 클래스를 통해 response 객체를 만들 수 있다

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('Body data', 200)
    # 1. flask.helpers.make_response 함수를 이용한 방법

    # 헤더를 설정해 보자
    response.headers['Something'] = 'Value'
    # werkzeug.datastructures.Headers 클래스의 인스턴스

    return response


@app.route('/2')
def index2():
    response = Response('Hello', 200)
    # 2. flask.wrappers.Response 클래스를 이용한 방법
    # flask.helpers에서 make_response를 뜯어보면, 결국은 Response 클래스를 이용해 객체를 만들어 낸다
    # https://github.com/pallets/flask/blob/master/flask/wrappers.py 가장 하단의 Response 클래스를 살펴보면 된다

    return response

app.run(debug=True)
