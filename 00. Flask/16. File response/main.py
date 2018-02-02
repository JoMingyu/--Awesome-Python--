from flask import Flask, send_from_directory, send_file
# flask 모듈의 send_from_directory나 send_file함수를 이용해 파일을 전송할 수 있다

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('./', 'sample.png')
    # mimetype, as_attachment, attachment_filename 등의 매개변수를 넘겨줄 수 있다

app.run(debug=True)
