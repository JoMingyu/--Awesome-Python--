# -- 알아볼 부분
# flask.blueprints.Blueprint - https://github.com/pallets/flask/blob/master/flask/blueprints.py#L79

from flask import Flask
from flask import Blueprint
# 플라스크는 어플리케이션을 블루프린트의 집합으로 고려한다. 이 방식은 대형 어플리케이션에 있어서 이상적이다
# Blueprint를 이용해 모듈간 협업이 가능하다

simple_blueprint = Blueprint('simple_blueprint', __name__)
# 블루프린트 객체를 얻는다. 파라미터는 name, import_name 순이다


@simple_blueprint.route('/')
def index():
    return 'hello'

app = Flask(__name__)
app.register_blueprint(simple_blueprint, url_prefix='/simple')
# 기존에 하던 것처럼 Flask 객체를 얻고, register_blueprint 메소드로 블루프린트를 등록한다
# url_prefix 옵션은 블루프린트가 동작할 기본 url prefix를 뜻한다

# 계정, 게시글 등 API category마다 나누어서 Blueprint를 나누고, 각 blueprint들을 app 객체에 모아주는 형태의 구조가 굉장히 좋다

if __name__ == '__main__':
    app.run(debug=True)
