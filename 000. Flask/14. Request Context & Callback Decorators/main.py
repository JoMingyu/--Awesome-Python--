# Request context는 요청을 처리하는 동안 요청 레벨의 데이터를 관리하기 위해 사용한다
# globals.request가 대표적인 request context에 해당하는 객체이다

# Flask 어플리케이션이 요청을 처리할 때, WSGI 서버로부터 받은 environment를 기반으로 Request 객체를 생성한다
# Worker(스레드, 프로세스, 코루틴 등)가 한 번에 하나의 요청만을 처리할 수 있기 때문이다.
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    # 요청을 처리할 때, Flask는 자동으로 request context를 push한다. 사용할 수 있는 scope는 appliction context와 동일하다
    return request.args['key']

# Application context와 동일하게, request context도 수동으로 push할 수 있다
with app.test_request_context('/?key=hello'):
    print(request.args['key'])

# --
# Request context에 관련하여, callback decorator라는 개념이 존재한다
# 매 요청 이전에 실행되는 함수, 매 요청이 끝나고 response하기 직전에 실행되는 함수 등을 정의할 수 있다
from flask import g

# 아래에서 정의하는 모든 데코레이터에 할당된 함수는 application/request context에 모두 접근할 수 있다

@app.before_first_request
def first_request():
    # 앱이 실행된 후 가장 첫 요청의 처리 전에 해당 함수가 호출
    print('Before first request')


@app.before_request
def before_request():
    # 매 요청의 처리 이전에 호출
    print('Before request')
    
    g.host = request.host
    g.remote_addr = request.remote_addr


@app.after_request
def after_request(response):
    # 매 요청이 처리되고 난 후, response하기 직전
    # after_request 데코레이터에 의해 데코레이팅된 함수는 response 객체를 받기 위한 인자를 정의해야 한다
    print('After request')

    # after_request라는 데코레이터를 사용하는 함수는 response 객체를 받는데, 이를 반환하기 직전까지 해야 할 작업을 수행하면 됨
    # CORS 헤더같은 것들을 얹어 주는 등의 일에 사용 가능
    response.headers['Custom-Header'] = 'Hello?'
    print(type(response))
    # flask.wrapper.Response 객체

    # response 객체를 직접 반환해 주어야 함
    return response


@app.teardown_request
def teardown_request(exception):
    # 매 요청이 끝난 다음
    print('Teardown request')


@app.teardown_appcontext
def teardown_appcontext(exception):
    # 요청의 처리가 완전히 끝나고 application context가 종료될 때 호출
    print('Teardown appcontext')

if __name__ == '__main__':
    app.run(debug=True)