from flask import Flask
from flask import send_from_directory, send_file
# flask.helpers 패키지의 send_from_directory나 send_file함수를 이용해 파일을 전송할 수 있다

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('./', 'sample.png')
    # path를 safe_join하고, 파일의 full path를 가져와 send_file로 제어를 넘기는 형태
    # mimetype, as_attachment, attachment_filename 등의 매개변수를 넘겨줄 수 있다

if __name__ == '__main__':
    app.run(debug=True)
