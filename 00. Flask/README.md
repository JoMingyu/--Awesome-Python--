# Flask
작고 강력한 파이썬의 서버 프레임워크
~~~
pip install flask
~~~
<https://github.com/pallets/flask>

장고보다 Star가 1400개나 더 많다!

## 개요
Python으로 작성된 마이크로 서버 프레임워크. 두개의 외부 라이브러리(Jinja2 템플릿 엔진, Werkzeug WSGI 툴킷)에 의존하고 있음. Flask의 '마이크로'는 핵싱 기능만 간결하게 유지하되 쉽게 확장 가능한 것을 목적으로 한다는 의미를 가지고 있다.

Flask는 내부적으로 Thread local 방식을 사용한다. Thread-safe한 상태를 유지하기 위해서 하나의 요청에서 함수들이 돌아가며 객체를 주고받을 필요가 없도록 했다. 이 때문에 문맥(Context)를 이해하는 일이 매우 중요하다.

## Flask best practices
[Flask Best Practicesd(일본어)] <https://github.com/yoshiya0503/Flask-Best-Practices/wiki>  
[Flask Hacks and Best Practices] <http://slides.skien.cc/flask-hacks-and-best-practices/>  
[Organizing your project - Flask 1.0 doc] <http://exploreflask.com/en/latest/organizing.html>  
[How to Structure Large Flask Applications] <https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications>

## 이상적인 구조
<https://github.com/JoMingyu/Flask-Large-Application-Example>

## 팁
1. request 데이터를 받는 문법에 따라, Flask는 응답을 자동으로 처리하는 경우가 있습니다.
~~~
1. request.args.get('test')
1번의 경우 test라는 파라미터가 없다면 None을 반환하기 때문에 파라미터를 보내지 않아도 분기에 문제가 생기지 않습니다.

2. request.args['test']
그러나 2번의 경우 test라는 파라미터가 없다면 KeyError가 날 수 있기 때문에, 요청에서 해당 파라미터가 없는 경우 Flask에서 자동으로 400 Bad Request를 반환합니다. 자동으로 Bad Request를 던져 주는건 좋지만, .get()의 기본값 처리나 타입 캐스팅의 메리트 덕분에 '1번 + required 데이터로 if를 돌려 400 처리하는 보일러플레이트'를 얹어서 사용하곤 합니다.
~~~
2. flask-restful의 Resource를 상속받아 API를 구현하게 되면 기본적으로 응답의 Content-Type이 application/json으로 처리됩니다.
3. flask-restful의 Resource 상속받아 API를 구현하여 ''를 리턴하면 ""로, None을 리턴하면 null로 반환됩니다. Content Type을 바꾸기 위해서는 Response를 보내기 위해선 Flask의 wrapper 클래스인 Response를 사용하면 됩니다.
~~~
from flask import Response
from flask_restful import Resource

class Test(Resource):
    def get(self):
        return Response('', 200)
~~~
4. Flask-JWT는 Flask 기반 JWT 라이브러리들 중 Star가 가장 많지만 개발이 중지된 상태이며 확장성이 그리 높지 않습니다. Flask-JWT-Extended 라이브러리를 사용하는 편이 더 좋습니다.
5. Swagger로 서버를 문서화했으나 API 문서를 정상적으로 불러오지 못한다면, 서버 측에서 CORS 헤더를 정상적으로 반환하는지 확인하기 바랍니다.
6. Flask의 한가지 단점은 인코딩 문제입니다. 모든 텍스트가 유니코드로 처리됩니다. 이를 해결하기 위해선 json 모듈의 도움을 받아야 합니다.
~~~
import json

from flask import Flask, Response

app = Flask(__name__)
@app.route('/')
def index():
    body = {'key': '한글한글'}
    return Response(json.dumps(body, ensure_ascii=False), content_type='application/json; charset=utf8', 200)
~~~
헤더에 Content Type을 달아주는 건 @app.after_request 데코레이터를 통해 해결할 수 있을 것입니다.
