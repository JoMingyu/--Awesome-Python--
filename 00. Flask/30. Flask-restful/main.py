from flask import Flask, Blueprint
from flask_restful import Api
# pip install flask-restful
# Flask 공식 문서에선 별도로 언급하지 않는, Flask로 REST API를 구현하기 위한 좋은 모듈

blueprint = Blueprint('sample_blueprint', __name__)
api = Api(blueprint)
# Api 클래스의 생성자에 Flask 인스턴스를 전달하며 api 객체를 얻어냄

from index import Index
api.add_resource(Index, '/')
# api 객체의 add_resource 메소드를 이용해 리소스와 uri를 매핑

app = Flask(__name__)
app.register_blueprint(blueprint)
# 블루프린트 등록

if __name__ == '__main__':
    app.run(debug=True)
