from datetime import timedelta

from flask import Flask, request, jsonify

from flask_jwt_extended import JWTManager, get_jwt_identity
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import create_refresh_token, jwt_refresh_token_required
# pip install flask-jwt-extended
# flask-jwt 모듈은 솔직히 별로 좋지 않다. 무조건 User 모델을 만들어야 하고, 함수 기반으로 handler를 정의해야 한다
# 굉장히 폐쇄적인데다 개발이 중지되기도 했는데, 이를 flask-jwt-extended 패키지가 해결해준다
# create_access_token 함수로 access token을 만들 수 있으니, 기존 API들과 이식성을 많이 높일 수 있다


app = Flask(__name__)

app.config.update(
    SECRET_KEY='super secret',
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=1),
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=30),
    JWT_HEADER_TYPE='JWT'
)
# JWT_SECRET_KEY 설정도 있으나, 이게 설정되지 않았다면 SECRET_KEY를 참조한다
# Access token은 유효기간을 짧게, Refresh token은 유효기간을 길게 제공하여 자주 Refresh하도록 하는 것이 이상적이다

JWTManager(app)

user = {
    'planb': 'test_pw'
}


@app.route('/auth', methods=['POST'])
def auth():
    id = request.form.get('id')
    pw = request.form.get('pw')

    if not id:
        return jsonify({
            'msg': 'Missing id parameter'
        }), 400

    if not pw:
        return jsonify({
            'msg': 'Missing pw parameter'
        }), 400

    if id in user and user[id] == pw:
        return jsonify({
            'access_token': create_access_token(identity=id),
            'refresh_token': create_refresh_token(identity=id)
        }), 201

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
def protected():
    return jsonify({
        'identity': get_jwt_identity()
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
