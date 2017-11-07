from flask import Flask
# 미들웨어는 서버에 요청이 들어올 때마다 호출되는 코드. 파이썬에선 WSGI 미들웨어를 사용한다
# 이전에 배웠던 app 객체의 after_request 데코레이터와 비슷하다고 생각할 수 있다

from werkzeug.wrappers import Request
# Request 클래스를 통해 environ으로 request 객체를 얻어올 수 있다


class SampleMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ)
        print(req.args.get('test'))
        return self.app(environ, start_response)


class Middleware2(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('Second middleware')
        return self.app(environ, start_response)

app = Flask(__name__)
app.wsgi_app = SampleMiddleware(app.wsgi_app)
# wsgi_app 속성에 미들웨어의 인스턴스를 넣어준다

app.wsgi_app = Middleware2(app.wsgi_app)
# 여러개 등록 가능하다


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
