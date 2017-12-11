# npm run build 후 build의 결과물들을 templates와 static에 삽입
# index.html의 script src와 link href을 Jinja2 문법에 맞추어 url_for 형태로 바꾸기만 하면 됨
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
