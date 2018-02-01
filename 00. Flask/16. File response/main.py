from flask import Flask, send_from_directory
# flask 모듈의 send_from_directory 함수를 이용해 파일을 전송할 수 있다

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('./', 'sample.png')

app.run(debug=True)
