from datetime import timedelta

from flask import Flask, request, jsonify

# https://github.com/vimalloc/flask-jwt-extended
# pip install flask-jwt-extended
from flask_jwt_extended import JWTManager, get_jwt_identity
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import create_refresh_token, jwt_refresh_token_required
# create_access_token 함수로 access token을 만들 수 있으니, 기존 API들과 이식성을 많이 높일 수 있다


app = Flask(__name__)

app.config.update(
    SECRET_KEY='super secret',
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=1),
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=30),
    JWT_HEADER_TYPE='JWT'
    # 기본값은 'Bearer'
)
# JWT_SECRET_KEY 설정도 있으나, 이게 설정되지 않았다면 SECRET_KEY를 참조한다
# Access token은 유효기간을 짧게, Refresh token은 유효기간을 길게 설정하여 자주 Refresh하도록 하는 것이 이상적이다

JWTManager(app)
# app 객체의 config들을 이용해 JWT 관련 세팅 initialize

user = {
    'planb': 'test_pw'
}


@app.route('/auth', methods=['POST'])
def auth():
    id = request.form['id']
    pw = request.form['pw']

    if id in user and user[id] == pw:
        return jsonify({
            'access_token': create_access_token(identity=id),
            'refresh_token': create_refresh_token(identity=id)
        }), 200

    else:
        return jsonify({
            'msg': 'Incorrect id or password'
        }), 401


@app.route('/refresh')
@jwt_refresh_token_required
def refresh():
    return jsonify({
        'access_token': create_access_token(identity=get_jwt_identity())
    })


@app.route('/protected')
@jwt_required
# JWT access token이 헤더에 함께 전달되어야 view function이 호출됨
# 제대로 된 access token이 전달되지 않으면 401 반환
def protected():
    return jsonify({
        'identity': get_jwt_identity()
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
