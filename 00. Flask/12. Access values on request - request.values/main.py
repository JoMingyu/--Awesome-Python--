from flask import Flask, request

app = Flask(__name__)


# request 객체에서 args를 통해 query string, form을 통해 body-data를 받아올 수 있었다
@app.route('/', methods=['POST'])
def index():
    # args와 form을 믹스한게 하나 있는데, values라는 속성이다
    print(type(request.values))
    print(request.values['query-string'])
    print(request.values['form-data'])
    # 실제로 테스트해 보면, 파라미터로 주든 body로 주든 알아서 인식한다

    return 'hello'

app.run(debug=True)
