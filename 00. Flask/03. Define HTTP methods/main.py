from flask import Flask

app = Flask(__name__)
# 평범하게 객체를 생성하고


@app.route('/')
def index():
    return 'hello'
# '/'에 라우팅을 진행했다
# 근데 이게 기본으로 GET 메소드에서만 작동한다
# 대부분 웹서버는 HTTP 메소드를 지정해주어야 할 때가 많다


@app.route('/test', methods=['POST', 'ASD'])
def test():
    return 'POST!!!'
# POST가 아닌 메소드로 /test에 접근하면 status code 405(Method not allowed)가 반환된다
# methods는 위에서 보듯이 리스트로 전달하기 때문에 여러 HTTP 메소드를 지정할 수 있다
# 표준화된 HTTP 메소드가 지정되지 않더라도 오류는 뜨지 않는다
# 대/소문자에 영향을 받지 않는다. pOsT라고 써도 잘 된다

app.run(debug=True)
