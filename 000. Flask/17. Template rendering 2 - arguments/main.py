from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    user_name = request.args['userName']
    return render_template('index.html', username=user_name)
    # 템플릿에 위와 같은 방식으로 변수를 넘겨준다(가변인자)

app.run(debug=True)
