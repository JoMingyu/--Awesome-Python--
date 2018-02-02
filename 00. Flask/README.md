# Flask
작고 강력한 파이썬의 서버 프레임워크
~~~
pip install flask
~~~
<https://github.com/pallets/flask>

## 개요
Python으로 작성된 마이크로 서버 프레임워크. 두개의 외부 라이브러리(Jinja2 템플릿 엔진, Werkzeug WSGI 툴킷)에 의존하고 있음. Flask의 '마이크로'는 핵싱 기능만 간결하게 유지하되 쉽게 확장 가능한 것을 목적으로 한다는 의미를 가지고 있다.

Flask는 내부적으로 Thread local 방식을 사용한다. Thread-safe한 상태를 유지하기 위해서 하나의 요청에서 함수들이 돌아가며 객체를 주고받을 필요가 없도록 했다. 이 때문에 문맥(Context)를 이해하는 일이 매우 중요하다.

## 주의사항
Flask 자체에 내장된 WSGI 서버는 배포용으로 설계된 것이 아니므로, production level에서 서버를 구동시킬 경우 gunicorn이나 uWSGI와 같은 적절한 WSGI 서버를 붙여 주는 것이 좋습니다.

## Flask best practices
<a href="https://github.com/yoshiya0503/Flask-Best-Practices/wiki">Flask Best Practices(일본어)</a>  
<a href="http://slides.skien.cc/flask-hacks-and-best-practices">Flask Hacks and Best Practices</a>  
<a href="http://exploreflask.com/en/latest/organizing.html">Organizing your project - Flask 1.0 doc</a>  
<a href="https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications">How to Structure Large Flask Applications</a>

## 이상적인 구조
<a href="https://github.com/JoMingyu/Flask-Large-Application-Example">Flask Large Application Example</a>

## 팁
1. request.***(args, form 등) 객체는 dict-like object입니다. 따라서 request 데이터를 받는 문법에 따라, Flask는 응답을 자동으로 처리할 때가 있습니다.
~~~
1. request.args.get('test')
1번의 경우 test라는 파라미터가 없다면 None을 반환하기 때문에 파라미터를 보내지 않아도 분기에 문제가 생기지 않습니다.

2. request.args['test']
2번의 경우 test라는 파라미터가 없다면 KeyError가 발생합니다. Flask에서는 request에 대하여 KeyError가 발생할 경우 자동으로 400 Bad request를 응답합니다.
~~~
2. flask-restful의 Resource를 상속받아 API를 구현하게 되면 기본적으로 응답의 Content-Type이 application/json으로 처리됩니다. 따라서 view function에서 ''를 리턴하면 ""로, None을 리턴하면 null로 반환됩니다. Content Type을 text/html 등으로 바꾸기 위해서는 Flask의 wrapper 클래스인 Response를 사용하면 됩니다.
~~~
from flask import Response
from flask_restful import Resource

class Test(Resource):
    def get(self):
        return Response('', 200)
~~~
3. Flask-JWT는 Flask 기반 JWT 라이브러리들 중 Star가 가장 많지만 개발이 중지된 상태이며 확장성이 그리 높지 않습니다. Flask-JWT-Extended 라이브러리를 사용하는 편이 더 좋습니다.
4. Flask의 한가지 단점은 인코딩 문제입니다. 모든 텍스트가 유니코드로 처리됩니다. 응답 시 인코딩 문제를 해결하기 위해서는 json 모듈과 Response 클래스의 도움을 받아야 합니다.
~~~
import json

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    body = {'key': '한글한글'}
    return Response(json.dumps(body, ensure_ascii=False), content_type='application/json; charset=utf8', 200)
~~~
5. 400번 이상의 status code response는 abort() 함수를 사용하는 편이 더 좋습니다.
~~~
from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    abort(404)
~~~
