from flask import Flask
from flask import make_response
from flask import Response
# make_response() 함수 또는 Response 클래스를 통해 response 객체를 만들 수 있다

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('Body data', 200)
    # 1. helpers.make_response 함수를 이용한 방법

    # 헤더를 설정해 보자
    response.headers['Something'] = 'Value'
    # werkzeug.datastructures.Headers 클래스의 인스턴스

    return response


@app.route('/2')
def index2():
    response = Response('Hello', 200)
    # 2. wrappers.Response(werkzeug.wrappers.BaseResponse) 클래스를 이용하는 방법

    return response

if __name__ == '__main__':
    app.run(debug=True)
