# https://github.com/pallets/flask
# pip install flask
from flask import Flask
# 간단한 작업은 간단하게 할 수 있고, 큰 서버도 어렵지 않게 다룰 수 있다 = Flask는 핵심기능만 간결하게 유지하고, 확장 가능한 것을 목적으로 한다

app = Flask(__name__)
# [app.Flask]
#     def __init__(self, import_name, static_path=None, static_url_path=None,
#     static_folder='static', template_folder='templates', instance_path=None, instance_relative_config=False)
# 1. 현재 모듈에 대해 Flask 객체를 생성

@app.route('/')
# 2. 데코레이터를 통해 '/'에 라우팅. Flask 라우팅의 가장 기본형
# [app.Flask]
#     def route(self, rule, **options) - 'A decorator that is used to register a view function for a given URL rule'

# 위처럼 한 URL Rule에 대해 할당되어 로직을 처리하는 함수를 view function이라고 부른다
# URL rule - Endpoint에서 HTTP 메소드를 제외한 부분('GET /'에서 'GET'을 뺀 '/')
# 별도의 HTTP 메소드 명시가 없으면 GET에 라우팅하며, 따라서 아래의 view function은 'GET /'의 요청 처리를 담당
def index():
    return 'Hello World'
    # 요청이 들어오면, 문자열 'Hello World'를 응답으로 전달. status code는 별도로 명시하지 않으면 '200 OK'로 처리


@app.route('/custom/<int:param>')
# Path parameter 정의 - <type:name>, 타입은 생략할 수 있으며, 생략한다면 타입은 str로 처리
# 아래의 view function은 'GET /custom/{param}'에 대한 요청 처리를 담당
def custom(param):
    # Path parameter가 존재하면, view function에서 동일한 이름으로 인자를 받아 주어야 함
    # Path parameter에 타입이 명시되어 있으면 view function에 넘어오는 인자도 해당 타입으로 캐스팅됨
    return param

if __name__ == '__main__':
    app.run()
    # 3. 서버 run
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options)
    # 기본적으로 host='127.0.0.1'(localhost), port=5000에서 debug=False 상태로 동작한다
