from flask import Flask, Blueprint

# https://github.com/flask-restful/flask-restful
# pip install flask-restful
from flask_restful import Api
# Flask로 REST API를 구현하기 위한 좋은 라이브러리

blueprint = Blueprint('sample_blueprint', __name__)
api = Api(blueprint)
# Api 클래스의 생성자에 Flask 인스턴스나 Blueprint 전달하여 api 객체를 생성

from index import Index
api.add_resource(Index, '/')
# api 객체의 add_resource 메소드를 이용해 리소스와 uri를 매핑

app = Flask(__name__)
app.register_blueprint(blueprint)
# 블루프린트 등록

from flask_restful import Resource
# api 객체에 add_resource하는 방법도 있으나, 데코레이터를 이용할 수도 있음
@api.resource('/test')
class TestResource(Resource):
    def get(self):
        return {
            'msg': 'hello!'
        }
# 이를 통해 Flask 어플리케이션을 고도로 구조화할 수 있다
# - 모듈마다 api 객체를 가지고 있고, 한 곳에서 해당 객체의 blueprint를 묶어주는 구조

if __name__ == '__main__':
    app.run(debug=True)
