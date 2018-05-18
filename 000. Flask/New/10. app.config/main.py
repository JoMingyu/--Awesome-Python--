from flask import Flask

app = Flask(__name__)

app.config['CONFIG'] = 'hello?'
# app의 config를 통해 설정 값들을 저장할 수 있다

print(app.config['CONFIG'])
# [app.Flask]
#     self.config = self.make_config(...)
# 해당 객체는 config.Config 클래스의 인스턴스이며, 해당 클래스는 dict를 상속받고 있어 딕셔너리로 할 수 있는 일들을 모두 할 수 있다

app.config.update({
    'CONFIG_1': 1,
    'CONFIG_2': True
})
del app.config['CONFIG_2']
print('CONFIG_2' in app.config)

# --

print(app.config)
# 수많은 설정 값(DEBUG, TESTING, JSONIFY_MIMETYPE 등)들이 이미 들어가 있다(app.Flask.default_config)
# 이미 들어가 있는 해당 설정 값들의 일부는 프로퍼티 형태로 즉시 접근 가능하다
print(app.debug, app.testing, app.secret_key)

# app.config는 딕셔너리를 상속받고, config를 외부에서 load하기 위한 여러 메소드들을 정의해 두었다
# [app.Config]
#     def from_envvar(self, variable_name, silent=False)
#     def from_pyfile(self, filename, silent=False)
#     def from_object(self, obj)
#     ...
# 대표적으로 파이썬 모듈 기반, 클래스 기반, 환경 변수 기반, JSON으로 관리할 수 있다

class SomeConfig(object):
    SOME_CONFIG = 1

app.config.from_object(SomeConfig)
print(app.config['SOME_CONFIG'])
