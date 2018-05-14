from flask import Flask, jsonify

# https://github.com/mattupstate/flask-jwt
# pip install flask-jwt
from flask_jwt import JWT, jwt_required, current_identity
# Flask에서 JWT 기반 사용자 인증을 돕는 라이브러리
# star는 많지만, 이슈는 많은데 개발이 중단되어 있는 상태라 추천하기엔 많이 부족한 라이브러리
# + 맘에 들지 않는 제약조건도 상당함


class User:
    # 사용자 데이터를 다루는 클래스
    # id 속성은 아래의 authenticate에서 참조하기 때문에 꼭 들어가 있어야 한다
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw


users = [
    User('planb', 'test_pw'),
    User('user', 'pw')
]
# 사전에 사용자 데이터를 가지고 있도록 하자


def authenticate(userid, pw):
    # POST /auth에 대한 경로를 열어 Access token을 리턴해주는 역할의, 일종의 view function
    # JSON으로 구성된 요청 데이터에 접근하는데, JSON body의 username과 password에 해당하는 각각의 값이 이 함수의 인자에 순서대로 들어온다
    # /auth로 설정된 default url rule과 username, password key를 config를 통해 바꿀 수 있다
    for user in users:
        if user.id == userid and user.pw == pw:
            return user
            # 여기서 리턴하는 값은 id 속성이 선언되어 있는 사용자 데이터 클래스의 객체여야 한다
            # 페이로드의 'identity'에 이 객체가 가지고 있는 id 속성의 값이 들어간다


def identity(payload):
    # 서버의 다른 요소에선 페이로드에 직접 접근하지 않고 여기서 리턴해 주는 identity가 담긴 별도의 변수에 접근한다
    # 위에서 import한 current_identity에 값을 넣어주는 역할
    return payload['identity']
    # 여기서 리턴되는 페이로드는 werkzeug.local.LocalProxy 클래스로 wrapping되는데, 문자열로 캐스팅 가능하다
    # 이 wrapping 과정을 모르고 있으면 MongoDB에서 bson 관련 에러로 고생할 수 있다


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
# JWT security algorithm을 위해 secret key가 필요하다

app.config['JWT_AUTH_URL_RULE'] = '/auth-for-test'
app.config['JWT_AUTH_USERNAME_KEY'] = 'id'
app.config['JWT_AUTH_PASSWORD_KEY'] = 'pw'
# URL rule과 username, password key를 바꿔줄 수 있다

from datetime import timedelta
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=365)
# JWT_EXPIRATION_DELTA 옵션에 만료 시간을 설정할 수 있다. 기본값은 5분

JWT(app, authenticate, identity)


@app.route('/protected')
@jwt_required()
# JWT 토큰이 필요함을 명시한다
# JWT 토큰이 없으면 401 UNAUTHORIZED를 반환
def protected():
    return jsonify({
        'message': 'This is a protected resource.',
        'current_identity': str(current_identity)
    })


if __name__ == '__main__':
    app.run(debug=True)
