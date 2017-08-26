from flask import Flask, request

app = Flask(__name__)
# body 데이터를 다룰 일이 생기곤 한다


@app.route('/', methods=['POST'])
def index():
    return request.form['test_key']
    # body 데이터에 접근하는데, form-data와 urlencoded 모두 form으로 접근 가능하다

app.run(debug=True)
