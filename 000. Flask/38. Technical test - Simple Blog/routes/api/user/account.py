from flask_restful_swagger_2 import swagger, Resource, request
from database.models.user import User


class Signup(Resource):
    @swagger.doc({
        'tags': ['계정'],
        'description': '회원가입',

        'parameters': [
            {
                'name': 'id',
                'description': '사용자 ID',
                'in': 'formData',
                'type': 'String'
            },
            {
                'name': 'pw',
                'description': '사용자 비밀번호',
                'in': 'formData',
                'type': 'String'
            }
        ],

        'responses': {
            '201': {
                'description': '회원가입 성공'
            },
            '204': {
                'description': '회원가입 실패(ID 중복)'
            }
        }
    })
    def post(self):
        id = request.form.get('id')
        pw = request.form.get('pw')

        if User.objects(id=id):
            return '', 204
        else:
            User(id=id, pw=pw).save()
            return '', 201
