from flask import abort, request
from flask_restful import Resource
# flask-restful을 이용해 라우팅하려면, flask_restful.Resource 클래스를 이용한다
# flask_restful.Resource는 사실 Flask에서 플러거블 뷰의 메소드 기반 디스패치를 지원하기 위한 flask.views.MethodView 클래스를 상속받고 있다
# Resource 클래스를 상속받은 클래스는 하나의 uri에 대한 자원(REST에서 Resource)이 된다
# abort, request와 같이 flask에서 지원하는 필드들을 flask-restful에서도 지원하지만
# 단순히 중계할 뿐이므로(https://github.com/flask-restful/flask-restful/blob/master/flask_restful/__init__.py#L5-L7) 그냥 flask에서 가져오는 게 좋다


class Index(Resource):
    # HTTP 메소드를 그대로 클래스 메소드로 표현하며 이들은 각 endpoint에 대한 view function이 됨
    def get(self):
        print(request.args['key'])
        # 요청 데이터에 접근할 때, 해당 key가 존재하지 않는다면 자동으로 '400 bad request'를 abort해 준다

        return [1, 2, 3]
        # Flask의 route 데코레이터를 통한 라우팅에서 이 구문은 TypeError를 발생시키지만
        # Flask-restful의 Resource를 상속받아 API를 구현하면 반환이 자동으로 직렬화되며 Content Type이 application/json으로 처리됨

    def post(self):
        abort(400)
