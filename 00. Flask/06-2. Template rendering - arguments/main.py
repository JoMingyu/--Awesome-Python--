from flask import Flask, render_template, request

app = Flask(__name__)


# 템플릿에 변수를 얹어줘야 할 일이 생긴다
@app.route('/', methods=['GET'])
def index():
    user_name = request.args['userName']
    return render_template('index.html', username=user_name)
    # 해당 템플릿에 위와 같이 파라미터 방식으로 값을 넘겨준다

app.run(debug=True)
