from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def index():
    abort(400)
    # abort() 함수는 에러 코드를 가지고 일찍 요청을 중단시킨다
    # werkzeug.exceptions 모듈의 HTTPException 클래스를 상속받아 커스텀 상태 코드를 만들 수 있다(exceptions 모듈을 보면 알 수 있듯 정확히는 예외 코드다)
    # abort를 이용해 커스텀 상태 코드를 사용할 수 있게 된다

app.run(debug=True)
