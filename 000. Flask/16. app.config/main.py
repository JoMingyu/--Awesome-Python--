# -- 알아볼 부분
# flask.config.Config - https://github.com/pallets/flask/blob/master/flask/config.py#L40

from flask import Flask

app = Flask(__name__)

app.config['CONFIG'] = 'hello?'
# app의 config를 통해 설정 값들을 저장할 수 있다
# config를 계속 따라가다 보면, Flask에서 dict를 상속받은 클래스를 통해 config를 만들어내는 걸 볼 수 있다

print(app.config)
# 수많은 설정 값(DEBUG, TESTING, JSONIFY_MIMETYPE 등)들이 이미 들어가 있다
# https://github.com/pallets/flask/blob/master/flask/app.py#L271
# 이미 들어가 있는 해당 설정 값들은 app 객체의 프로퍼티 형태로 즉시 접근 가능하다
print(app.debug, app.testing, app.secret_key)

print(app.config['CONFIG'])

app.config['SECRET_KEY'] = 'qwe'
# config의 유명한 속성 중 하나는 이 secret key다. 타 패키지들이 자주 참조한다
# Flask의 세션에서 시큐어 쿠키를 구현하기 위한 key가 될 때도 있고
# JWT 토큰 암호화를 위한 key가 될 때도 있다
# 따라서 secret key는 환경 변수에서 관리해주는 편이 좋다

# Config 값은 대표적으로 파이썬 모듈 기반, 클래스 기반, 환경 변수 기반, JSON으로 관리할 수 있다
class SomeConfig(object):
    SOME_CONFIG = 1

app.config.from_object(SomeConfig)
print(app.config['SOME_CONFIG'])
