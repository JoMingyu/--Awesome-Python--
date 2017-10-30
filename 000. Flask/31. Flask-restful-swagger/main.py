from flask import Flask
from flask_cors import CORS
from flask_restful_swagger_2 import swagger, Api, Resource, request
# Swagger라는 멋진 API 관리 툴이 있는데, flask-restful-swagger 패키지를 이용해서 자동화 가능하다
# from flask_restful import Api 대신 위의 import 방식을 사용하자

app = Flask(__name__)
CORS(app)
api = Api(app, api_version='1.0')


class Sample(Resource):
    @swagger.doc({
        'tags': ['user'],
        # 태그를 기준으로 API 정리할 수 있다

        'description': 'Returns hello world!',
        # API description

        'parameters': [
            # 파라미터 리스트
            {
                'name': 'id',
                # 파라미터의 key name

                'description': 'Identifier',
                # 파라미터 description

                'in': 'path',
                # 파라미터가 들어갈 곳
                # must be path, query, header, body or formData

                'type': 'int'
                # 타입
            },
            {
                'name': 'test_form',
                'description': 'Data for test',
                'in': 'formData',
                'type': 'any'
            }
        ],
        'responses': {
            '200': {
                # status code

                'description': 'Success',
                # Response description

                'examples': {
                    # Example value
                    
                    'application/json': {
                        'id': 1,
                        'form_data': 'hello?'
                    }
                }
            }
        }
     })
    def post(self, id):
        return {
            'id': id,
            'form_data': request.form.get('test_form')
        }

api.add_resource(Sample, '/sample/<id>')

if __name__ == '__main__':
    app.run(debug=True)
