from flask import Flask
from flask import abort
# 내부에 'from werkzeug.exceptions import abort' 구문이 있음(실제로는 werzkeug.exceptions.abort에 의존)

app = Flask(__name__)


@app.route('/')
def index():
    abort(400)
    # [werkzeug.exceptions]
    #     def abort(status, *args, **kwargs)
    # abort() 함수는 HTTP 예외 코드(400번대 이상의 상태 코드)를 리턴해주는 역할을 한다

if __name__ == '__main__':
    app.run(debug=True)
