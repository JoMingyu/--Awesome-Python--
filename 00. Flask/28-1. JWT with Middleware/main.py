# 타 모듈의 도움을 받을 수 있지만, '일단' 없이 해보자
# 배워 둔 미들웨어를 쓰면, 어느 정도 페이로드 관리를 해줄 수 있다
from flask import Flask, request
from werkzeug.wrappers import Request
import jwt

payload = None


class JWTTracker:
    def __init__(self, app, secret_key):
        # 생성자에선 app 객체와 함께 JWT 암호화를 위한 secret key를 받도록 한다
        self.app = app
        self.secret_key = secret_key

    def __call__(self, environ, start_response):
        req = Request(environ)
        # environ을 request로 wrap
        if 'authorization' in req.headers:
            # 헤더에 authorization이 있다면

            jwt_token = req.headers.get('authorization', type=str)[7:]
            # 앞의 Bearer를 제거하기 위해 슬라이스

            global payload
            payload = jwt.decode(jwt_token.encode('utf-8'), self.secret_key, 'HS256')
            # global data에 접근해 페이로드를 저장

        return self.app(environ, start_response)

app = Flask(__name__)
app.secret_key = '!owkiaMM.zkai('
app.wsgi_app = JWTTracker(app.wsgi_app, app.secret_key)


users = {
    'planb': 'test_pw'
}
# 미리 정의해 둔 사용자


@app.route('/auth', methods=['POST'])
def index():
    username = request.form.get('username')
    pw = request.form.get('pw')

    if users[username] == pw:
        # 로그인 성공 시

        data = {'token': jwt.encode({'username': username, 'pw': pw}, app.secret_key, 'HS256').decode('utf-8')}
        return str({'token': data}), 201
        # JWT 토큰 제공

    else:
        return '', 204


@app.route('/private', methods=['GET'])
def private():
    return str(payload)


if __name__ == '__main__':
    app.run(debug=True)
    # 되도록이면 flask를 위해 제공되는 flask-jwt를 쓰는 게 편하다
