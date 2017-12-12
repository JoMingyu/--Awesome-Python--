from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
# pip install flasgger
# https://github.com/rochacbruno/flasgger

# Flask를 위한 Swagger 패키지
# flask-restful-swagger는 기존 flask-restful 앱에 적용하긴 좋지만 flask-restful에 너무 종속적이라는 단점이 있음
# Documentation 방식도 여러가지라서 선택지가 많지만 기본 상태는 Swagger UI Version 2로 동작하기 때문에 UI가 똥망
# 따라서 아래의 config에서 통해 ui version을 3으로 바꿔 주도록 하자

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'Sample',
    # 아래의 title과 다름. 여기는 HTML head에 들어가는 title
    'specs_route': '/docs/',
    # Swagger doc 라우팅 위치. leading/trailing slash가 꼭 있어야 함
    'uiversion': 3,
    # 기본값은 UI Version 2인데 UI가 똥망이니 3으로 변경하도록 하자

    'info': {
        'title': 'Sample Doc',
        'version': '1.0',
        'description': 'More Chicken'
    },
    # Swagger doc에 대한 기본 정보

    'host': 'localhost',
    'basePath': '/ ',
    # Title 바로 아래에 위치할 Base URL
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
# config와 template의 경계가 조금 애매하지만, 세팅 종류가 굉장히 많으니 그러려니 하고 넘어가는 편이 좋다

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


app.run(debug=True)
