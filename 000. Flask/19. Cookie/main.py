from flask import Flask, make_response, request
# 모두 알다시피 HTTP는 connectionless와 stateless라는 특징을 가진다
# 한번의 요청-응답이 이루어지고 나면 접속을 끊으며, 통신이 끝나면 상태 정보를 유지하지 않는다
# 그래서 쿠키와 세션을 사용한다

app = Flask(__name__)


# 쿠키를 주는거랑 쿠키를 검증하는 라우팅 두개를 하기로 했다
@app.route('/cookie', methods=['GET'])
def send_cookie():
    # 쿠키를 주려면 response 객체가 필요하다
    response = make_response('hello hello')
    response.set_cookie('cookie', 'value!!!!!!!!!')

    return response


@app.route('/cookie', methods=['POST'])
def verify_cookie():
    # 쿠키를 받으려면 request.cookies에 접근하자
    # 파라미터와 body를 받았을 때처럼 얘도 딕셔너리
    print(request.cookies['cookie'])

    # 쿠키 제거는
    response = make_response('hello hello!')
    response.set_cookie('cookie', '', expires=0)

    return response

app.run(debug=True)
