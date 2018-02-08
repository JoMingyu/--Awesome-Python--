# -- 알아볼 부분
# flask.helpers.send_from_directory() - https://github.com/pallets/flask/blob/master/flask/helpers.py#L667
# flask.helpers.send_file() - https://github.com/pallets/flask/blob/master/flask/helpers.py#L439

from flask import Flask
from flask import send_from_directory
from flask import send_file
# flask 모듈의 send_from_directory나 send_file함수를 이용해 파일을 전송할 수 있다

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('./', 'sample.png')
    # path를 safe_join하고, 파일의 full path를 가져와 send_file로 제어를 넘기는 형태
    # mimetype, as_attachment, attachment_filename 등의 매개변수를 넘겨줄 수 있다

app.run(debug=True)
