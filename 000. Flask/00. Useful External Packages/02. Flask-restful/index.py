from flask import abort
from flask_restful import Resource
# flask_restful의 Resource 클래스를 이용한다
# flask.restful.Resource는 사실 Flask에서 플러거블 뷰의 메소드 기반 디스패치를 지원하기 위한 flask.views.MethodView 클래스를 상속받고 있다
# Resource 클래스를 상속받은 클래스는 하나의 uri에 대한 자원(resource)이 된다
# abort, request와 같이 flask에서 지원하는 필드들을 flask-restful에서도 지원하지만 그냥 flask에서 가져오는 게 좋다


class Index(Resource):
    # app.route() 방식으로 라우트했던 게 메소드화 되었다
    def get(self):
        return [1, 2, 3]
        # Flask의 route 데코레이터를 통한 라우팅에서 이 구문은 TypeError를 발생시키지만
        # Flask-restful의 Resource를 상속받아 API를 구현하면 리턴의 Content Type이 application/json으로 처리됨

    def post(self):
        abort(400)
