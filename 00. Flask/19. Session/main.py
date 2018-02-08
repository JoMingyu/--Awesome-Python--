# -- 알아볼 부분
# flask.globals.session - https://github.com/pallets/flask/blob/master/flask/globals.py#L60

from flask import Flask, request, session
# session이라는 객체가 있다. 얘는 세션을 사용하는 데에 도움을 준다
print(type(session))
# LocalProxy 클래스의 객체지만 거의 딕셔너리처럼 사용할 수 있다

# Flask는 세션을 시큐어 쿠키를 통해 구현한다. 암호화를 사용해 그 쿠키를 서명한다는 뜻이다
# 사용자는 쿠키의 내용을 볼 수는 있지만 서명을 위해 사용된 비밀키를 모른다면 내용을 변경할 수 없다는 것을 의미한다
# 따라서 세션을 사용하기 위한 비밀 키를 설정해 두어야 한다
app = Flask(__name__)
app.secret_key = 'akqwoe1ifiasdfooidfom'
# 실제로 서버를 배포해야 한다면, 비밀 키는 환경 변수에서 가져오도록 하자


@app.route('/', methods=['GET', 'POST', 'DELETE'])
def session_test():
    if request.method == 'DELETE':
        session.pop('username')
        # 세션 삭제

        return 'Session deleted!'
    else:
        if 'username' in session:
            # 세션 존재 여부 검사
            
            return 'Hello {0}'.format(session['username'])
        else:
            session['username'] = request.values['username']
            # 세션 추가

            return 'Session appended!'

app.run(debug=True)
