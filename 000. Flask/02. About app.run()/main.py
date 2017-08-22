# 일단 Flask 어플리케이션은 대부분 아래의 구문들로 시작한다
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'

# app.run()
# run 메소드를 통해서 앱을 실행시키는데, 기본적으로 localhost:5000에 열린다
# host, port, debug 매개변수가 있다
app.run(host='127.0.0.1', port=9055, debug=True)
# 배포 단계가 아니라면 debug 매개변수를 True로 주는 게 좋다
# 코드의 Change detect를 해준다. 코드가 바뀌면 재시작해줌.
