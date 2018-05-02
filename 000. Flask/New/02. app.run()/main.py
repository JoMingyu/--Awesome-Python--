from flask import Flask

app = Flask(__name__)

# 라우팅
@app.route('/')
def index():
    return 'hello'

# 이후 run 메소드를 통해서 앱을 실행(서버를 시작)
# [app.Flask]
#     def run(self, host=None, port=None, debug=None, load_dotenv=True, **options)
# **options : app.run()에서 내부적으로 호출하는 werkzeug.serving.run_simple() 메소드에서 사용될 use_evalex, use_reloader, use_debugger, threaded 등의 파라미터들

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9055, debug=True, threaded=True)
    # host, port, debug의 기본값은 각각 '127.0.0.1'(localhost), 5000, False
    # debug는 보편적으로 생각하는 debug 모드를 뜻하는데, 특별한 점은 프로젝트 내에서 파일이 수정되면 자동으로 서버를 restart해 준다는 것

    # -- threaded=True
    # 일반적으로 Flask에 포함된 WSGI 서버는 단일 스레드 모드로 실행되며, 한 번에 하나의 요청만 처리할 수 있음
    # 따라서 병렬적으로 요청이 들어오면 처리할 수 있을 때까지 기다려야 하므로 문제 발생 가능
    # threaded 파라미터를 True로 전달하며 요청을 모두 새로운 스레드에서 처리하도록 만들어줄 수 있음

    # ** 서버가 동시에 처리할 수 있는 스레드 수는 SocketServer.ThreadingMixIn 클래스를 사용하는데, 기본적으로 스레드 수에 제한을 설정하지 않으므로
    # 프로덕션 전용으로 서버를 구동하려면 gunicorn이나 uWSGI와 같은 적절한 WSGI 서버를 붙여 주는 것이 좋음
