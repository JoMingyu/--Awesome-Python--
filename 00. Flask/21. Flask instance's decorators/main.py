from flask import Flask, request

# -- 알아볼 부분
# flask.app.Flask.before_request() - https://github.com/pallets/flask/blob/master/flask/app.py#L1415
# flask.app.Flask.before_first_request() - https://github.com/pallets/flask/blob/master/flask/app.py#L1429
# 등등

app = Flask(__name__)
# Flask 인스턴스에는 route() 말고도 유용하게 사용할만한 데코레이터들이 있다


@app.before_first_request
# https://github.com/pallets/flask/blob/master/flask/app.py#L1429
def first_request():
    # 앱이 실행된 후 가장 첫 요청 시
    print('Before first request')


@app.before_request
# https://github.com/pallets/flask/blob/master/flask/app.py#L1415
def before_request():
    # 매 요청이 처리되기 전에
    # 여기서도 request 객체에 접근할 수 있다
    # 로깅 용도로 사용하기 좋을 거 같다
    print('Before request :', request.host)


@app.after_request
# https://github.com/pallets/flask/blob/master/flask/app.py#L1442
def after_request(response):
    # 매 요청이 처리되고 난 후
    print('After request')

    # after_request라는 데코레이터를 사용하는 함수는 response 객체를 받는데, 이를 반환하기 직전까지 해야 할 어떤 일을 수행하면 됨
    # CORS 헤더같은 것들을 얹어 주는 것에 용이하게 사용할 수 있을 듯
    response.headers['Custom-Header'] = 'Hello?'
    # 여기서 받는 response 객체는 flask.wrapper.Response 클래스의 인스턴스
    print(type(response))

    # after_request 데코레이터를 사용하는 함수를 만들었을 경우 response 객체를 반환하는 구문이 필요함
    return response


@app.teardown_request
# https://github.com/pallets/flask/blob/master/flask/app.py#L1456
def teardown_request(exception):
    # 매 요청이 끝난 다음
    print('Teardown request')


@app.teardown_appcontext
# https://github.com/pallets/flask/blob/master/flask/app.py#L1494
def teardown_appcontext(exception):
    # 요청의 처리가 완전히 끝나고 Flask 어플리케이션 컨텍스트가 끝날 때마다 실행
    print('Teardown appcontext')


@app.route('/')
def index():
    print('-- Access')
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
