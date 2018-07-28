from flask import Flask
# 미들웨어는 서버에 요청이 들어올 때마다 호출되는 코드. Flask에서는 Werkzeug에서 제공되는 WSGI 미들웨어를 사용한다
# Flask에서 내부적으로 요청을 디스패칭할 때도 Werkzeug의 미들웨어를 사용한다

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