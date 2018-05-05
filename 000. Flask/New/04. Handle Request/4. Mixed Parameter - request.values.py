from flask import Flask, request

app = Flask(__name__)

# request.args로 Query Parameter, request.form으로 Form Parameter를 받아올 수 있었다
@app.route('/', methods=['POST'])
def index():
    # args와 form은 request.values 객체에 섞여 있다
    print(type(request.values))
    print(request.values['query-param'])
    print(request.values['form-param'])
    # values는 CombinedMultiDict의 인스턴스이며, 말 그대로 request.args와 request.form이 MultiDict 타입으로 각각 들어있다

    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
