from flask import Flask
from flask import Blueprint
# 플라스크는 어플리케이션을 블루프린트의 집합으로 고려한다
# Blueprint 객체에는 Flask 객체와 유사한 API가 구현되어 있어, 모듈화된 Flask 어플리케이션의 구조를 만들기에 적합하다
# -> Flask 클래스와 동일하게, helpers._PackageBoundObject를 상속받고 있다

simple_blueprint = Blueprint('simple_blueprint', __name__)
# [blueprints.Blueprint]
#     def __init__(self, name, import_name, static_folder=None, static_url_path=None,
#     template_folder=None, url_prefix=None, subdomain=None, url_defaults=None)
# 블루프린트 객체를 얻는다. 파라미터는 name, import_name 순이이며 name은 중복될 수 없다
# 모듈마다 한 블루프린트를 만든다면, 둘 다 __name__으로 채워 줘도 좋다


@simple_blueprint.route('/')
# Flask 객체와 유사한 라우팅 API
def index():
    return 'hello'

app = Flask(__name__)
app.register_blueprint(simple_blueprint, url_prefix='/prefix')
# [app.Flask]
#     def register_blueprint(self, blueprint, **options)
# 기존에 하던 것처럼 Flask 객체를 얻고, register_blueprint 메소드로 블루프린트를 등록한다
# 여기서는 '/prefix'라는 URL prefix를 해당 블루프린트에 달아 주었다

if __name__ == '__main__':
    app.run(debug=True)
