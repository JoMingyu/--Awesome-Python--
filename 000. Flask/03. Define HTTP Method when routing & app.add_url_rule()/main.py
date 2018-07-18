from flask import Flask

app = Flask(__name__)

# Flask에선 라우팅을 위한 여러 가지 방법들을 지원하고 있다
# 아래는 튜토리얼 등에서 보편적으로 사용하는 데코레이터 형태의 라우팅
@app.route('/')
def index():
    # 이전에도 말했듯, 별도의 HTTP 메소드 명시가 없으면 GET에 라우팅
    return 'GET /'


@app.route('/post-test', methods=['POST'])
# route 데코레이터에 methods 파라미터를 iterable 객체로 전달하여 다른 HTTP 메소드에 대해 라우팅
# -> app.Flask.route(self, rule, **options)의 **options에 해당
def index_post():
    # 해당 view function은 'POST /'의 요청 처리를 담당
    # POST가 아닌 메소드로 '/post-test'에 접근하면 status code '405 Method Not Allowed'가 반환된다
    return 'POST /'

# route 데코레이터의 코드를 보면, 내부적으로 self.add_url_rule 메소드를 호출하여 실제로 라우팅을 진행
# [app.Flask]
#     def add_url_rule(self, rule, endpoint, f, **options)
app.add_url_rule('/2', 'something', lambda: 'Hi!')
# endpoint는 해당 URL rule에 대한 endpoint 이름을 말하며, app.route() 시에는 view function의 이름을 사용

if __name__ == '__main__':
    app.run()
