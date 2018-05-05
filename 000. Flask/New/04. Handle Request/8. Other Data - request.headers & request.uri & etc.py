from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    # request 객체에는 수많은 속성들이 존재한다
    # werkzeug.wrappers.BaseRequest에서 @cached_property나 @property로 처리된 프로퍼티들에 접근할 수 있다
    print(request.host, request.remote_addr)
    print(request.method, request.uri, request.full_url)
    print(request.headers)
    print(request.is_xhr)

    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
