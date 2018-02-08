from flask import Flask, request

app = Flask(__name__)


# request.args로 querystring, request.form으로 form-data나 urlencoded 데이터를 받아올 수 있었다
@app.route('/', methods=['POST'])
def index():
    # args와 form을 믹스한게 하나 있는데, values라는 속성이다
    print(type(request.values))
    print(request.values['query-string'])
    print(request.values['form-data'])
    # values는 CombinedMultiDict의 인스턴스이며, querystring과 form-data/urlencoded 데이터가 MultiDict 타입으로 각각 들어있다

    return 'hello'

app.run(debug=True)
