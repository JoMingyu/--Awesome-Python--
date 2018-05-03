# [Flask](https://github.com/pallets/flask)
작고 강력한 파이썬의 웹 프레임워크
~~~
pip install flask
~~~

~~~
from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def index(name):
    return 'Hello {}'.format(name)


if __name__ == '__main__':
    app.run(port=3118, debug=True)
~~~

## 개요
Python으로 작성된 마이크로 웹 프레임워크. 두개의 외부 라이브러리(Jinja2 템플릿 엔진, Werkzeug WSGI 툴킷)에 의존하고 있습니다. Flask의 '마이크로'는 핵심 기능만 간결하게 유지하되 쉽게 확장 가능한 것을 목적으로 한다는 의미를 가지고 있습니다.

Flask는 내부적으로 Thread local 방식을 사용합니다. Thread-safe한 상태를 유지하기 위해서 요청 당 하나의 스레드에서 함수들이 돌아가며 객체를 주고받을 필요가 없도록 했습니다. 이 때문에 문맥(Context)를 이해하는 일이 매우 중요합니다.

2018년 4월 27일 새벽, [Flask 1.0이 릴리즈](https://github.com/pallets/flask/releases/tag/1.0)되었고, 해당 디렉토리의 예제들은 Flask 0.12.x와 Flask 1.0을 비교 설명하는 부분이 일부 포함되어 있습니다.

## 주의사항
Flask 어플리케이션을 실행하기 위한 다양한 방법이 있지만, 운영 단계에서는 Flask에 내장된 WSGI 서버를 사용하지 않기 바랍니다. Flask 1.0에서는 빨간 색의 경고문까지 출력됩니다. 배포용으로 설계되지 않았기 때문입니다. Apache의 mod_wsgi, 독립적인 WSGI 컨테이너(Gunicorn, Tornado 등), uWSGI, FastCGI, CGI 등을 사용할 수 있습니다.
