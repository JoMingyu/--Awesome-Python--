from flask import Flask, abort

app = Flask(__name__)


@app.errorhandler(404)
# [app.Flask]
#     def errorhandler(self, code_or_exception)
# 서버에서 반환하는 HTTP 예외 코드(400번대 이상)나 비즈니스 로직에서 일어나는 exception을 관리할 수 있다
# ex) 모든 404 not found에 대하여 커스텀 404 페이지 리턴(https://github.com/adsfokow 처럼), 모든 Exception에 대하여 로깅 등
def error(e):
    # 서버가 404를 반환하려 한다면, 해당 함수가 호출된다
    print(type(e))
    # werkzeug.exceptions.*** 타입
    print(e)
    # e는 에러 코드와 에러 메시지를 그대로 가지고 있다
    return 'hello'


@app.route('/')
def test():
    abort(404)


@app.errorhandler(AssertionError)
# view function에서 발생하는 AssertionError를 intercept하여 처리
def assertion_error(e):
    return 'AssertionError :(', 500


@app.route('/2')
def test2():
    raise AssertionError()

# view function에서 400, 500번대 status code를 반환하는 경우, 내부적으로는 'HTTPException'이 발생하는 것이므로
# errorhandler를 'Exception'에 대해 크게 잡는 경우 인스턴스를 체크하여 HTTPException인 경우 그에 맞는 status code를 response하는 것이 좋다
if __name__ == '__main__':
    app.run(debug=True)
