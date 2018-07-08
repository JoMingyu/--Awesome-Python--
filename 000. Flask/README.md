# [Flask](https://github.com/pallets/flask)
파이썬의 대표적인 마이크로 웹 프레임워크

```
pip install flask
```

```
from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def index(name):
    return 'Hello {}'.format(name)


if __name__ == '__main__':
    app.run(port=3118, debug=True)
```

## 개요
- Jinja2를 템플릿 엔진으로 의존
- Werkzeug를 WSGI 툴킷으로 의존
- 요청 당 하나의 스레드를 생성하여 처리하는 멀티 스레드 기반 구조
- 다양한 방식의 라우팅 지원(데코레이터, Pluggable View, low-level API들)
- 대부분의 웹 프레임워크들과 다르게 context를 콜백의 인자가 아닌 글로벌 객체에서 관리함
- 동일한 글로벌 객체가 요청마다 다른 값을 가지는 thread local 방식 사용
- 요청 데이터 접근에 대한 직관적 API 제공
- Blueprint 객체 + Flask 객체의 register_blueprint 메소드를 이용한 어플리케이션 구조화 지원
- Application context와 before_request, after_request 등의 데코레이터를 이용한 미들웨어 개념 지원
- 프레임워크 자체에서 지원하는 test client를 통한 테스트 지원

[공식 문서](http://flask.pocoo.org/docs/1.0/quickstart/#quickstart)가 정말 친절합니다. 2018년 4월 27일 새벽, [Flask 1.0이 릴리즈](https://github.com/pallets/flask/releases/tag/1.0)되었고, 해당 디렉토리의 예제들은 Flask 0.12.x와 Flask 1.0을 비교 설명하는 부분이 일부 포함되어 있습니다.

## 주의사항
Flask 어플리케이션을 실행하기 위한 다양한 방법이 있지만, 운영 단계에서는 Flask에 내장된 WSGI 서버를 사용하지 않기 바랍니다. Flask 1.0에서는 빨간 색의 경고문까지 출력됩니다. 배포용으로 설계되지 않았기 때문입니다. Apache의 mod_wsgi, 독립적인 WSGI 컨테이너(Gunicorn, Tornado 등), uWSGI, FastCGI, CGI 등을 사용할 수 있습니다.
