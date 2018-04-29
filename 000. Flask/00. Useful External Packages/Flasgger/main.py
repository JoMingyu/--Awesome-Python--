from flask import Flask, jsonify, request

# https://github.com/rochacbruno/flasgger
# pip install flasgger
from flasgger import Swagger, swag_from

# Flask에서 Swagger API documentation을 구현하기 위한 라이브러리
# flask-restful-swagger는 기존 flask-restful 앱에 적용하긴 좋지만 flask-restful에 너무 종속적이라는 단점이 있음
# flasgger는 Documentation 방식이 여러가지라 확장성이 매우 높음
# flasgger는 기본적으로 Swagger UI Version 2로 동작하기 때문에 아래의 config에서 통해 ui version을 3으로 바꿔 주도록 하자

app = Flask(__name__)
port = 5000

app.config['SWAGGER'] = {
    # Swagger를 위한 메타 데이터들
    'title': 'Sample',
    # 아래의 title과 다르게, 여기는 HTML head에 들어가는 title
    'specs_route': '/docs',
    # Swagger doc 라우팅 위치
    'uiversion': 3,
    # UI version 변경

    'info': {
        'title': 'Sample Doc',
        'version': '1.0',
        'description': 'More Chicken'
    },
    # Swagger doc에 대한 기본 정보

    'host': 'localhost:{}'.format(port),
    'basePath': '/ ',
    # Title 바로 아래에 위치할 Base URL
    # '[ Base url: {}{} ]'.format(host, basePath) 형태로 보여짐
}

template = {
    'schemes': [
        'http'
    ],
    'tags': [
        {
            'name': 'hi',
            'description': 'hi Tag Description'
        }
    ]
    # 각 태그들에 대해 미리 명시
}
# config.SWAGGER와 template의 경계가 조금 애매하지만 익숙해지면 크게 문제될 것 없음

swagger = Swagger(template=template)
swagger.init_app(app)


@app.route('/')
@swag_from({
    'tags': ['hi'],
    'parameters': [
        {
            'name': 'id',
            'in': 'query',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Success. Responses Your ID',
            'examples': {
                'ID': 'abcd'
            }
        }
    }
})
def index():
    """
    Example API
    """
    return jsonify({
        'ID': request.args.get('id')
    }), 200


app.run(debug=True, port=port)
