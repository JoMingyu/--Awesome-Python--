from flask import Flask, Response, request
# HTTP는 connectionless와 stateless라는 특징을 가진다
# 한번의 요청-응답이 이루어지고 나면 접속을 끊으며, 통신이 끝나면 상태 정보를 유지하지 않는다
# 그래서 쿠키나 세션을 사용하여 의도적으로 statefull한 상황을 만든다

app = Flask(__name__)


# 쿠키를 발급하는 view function과 쿠키를 검증하는 view function을 따로 두도록 하자
@app.route('/cookie', methods=['GET', 'POST'])
def send_cookie():
    if request.method == 'GET':
        # 쿠키를 주려면 Response 객체가 필요하다
        response = Response('hello hello')
        response.set_cookie('cookie', 'value!!!!!!!!!')
        # [werkzeug.wrappers.BaseResponse]
        #     def set_cookie(
        #         self, key, value='', max_age=None, expires=None, path='/',
        #         domain=None, secure=False, httponly=False, samesite=None
        #     )

        return response
    elif request.method == 'POST':
        # 쿠키를 받으려면 BaseRequest의 프로퍼티인 'cookies'에 접근
        print(request.cookies['cookie'])

        # 쿠키 제거는 expires를 0으로 주면 된다
        response = Response('hello hello!')
        response.set_cookie('cookie', '', expires=0)

        return response
    else:
        return '', 405

if __name__ == '__main__':
    app.run(debug=True)
