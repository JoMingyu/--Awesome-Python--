# -- 알아볼 부분
# flask.templating.render_template() - https://github.com/pallets/flask/blob/master/flask/templating.py#L121

from flask import Flask
from flask import render_template

app = Flask(__name__)

# 서버 사이드 렌더링 방식의 웹서버라면 꼭 가지고 있어야 할 기능인 템플릿 렌더링
# Flask는 Jinja2라는 템플릿 엔진을 내장하고 있다
# ejs같은 이상한 확장자가 아니라 그냥 html 그대로 쓴다!

# 주의해야 할 것은, Flask는 templates라는 폴더에서 템플릿을 찾는다는 점이다
# templates라는 폴더는 Flask 인스턴스가 초기화되는 곳과 같은 level의 디렉토리에 위치해야 한다
# 물론 Flask 인스턴스 초기화 과정에서 템플릿 디렉토리를 변경할 수 있다
# flask.app.Flask.__init__() - https://github.com/pallets/flask/blob/master/flask/app.py#L341


@app.route('/index')
def index():
    return render_template('test.html')

app.run(debug=True)

# Flask에 내장되어 있는 템플릿 엔진은 쉽게 바꿀 수 있다
