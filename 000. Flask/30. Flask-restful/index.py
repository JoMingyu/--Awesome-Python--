from flask_restful import Resource, abort
# flask_restful의 Resource 클래스를 이용한다
# Resource 클래스를 상속받은 클래스는 하나의 uri에 대한 자원(resource)이 된다
# Flask에서 사용하던 여러가지 리소스들은 flask-restful에서도 제공된다


class Index(Resource):
    # app.route() 방식으로 라우트했던 게 메소드화 되었다
    def get(self):
        return [1, 2, 3]
        # Flask의 route 데코레이터를 통한 라우팅에서 이 구문은 TypeError를 발생시키지만
        # flask-restful은 이를 알아서 처리해주는 듯 하다

    def post(self):
        abort(400)
