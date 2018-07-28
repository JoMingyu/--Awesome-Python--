from flask import Flask
from flask import request

app = Flask(__name__)
# GET에서 자주 사용하는 Query Paramter( = querystring(ex - localhost:5000/?a=1&b=2에서 물음표 뒷부분인 a=1&b=2) )에 접근하도록 하자
# 대부분의 웹 프레임워크에서는 요청 데이터 등과 같은 context 데이터들은 콜백의 인자로 전달하지만, Flask에서는 전역 객체를 사용한다
# flask.globals.request에 접근하면 되며, 이는 Request context와 연관되어 있는 객체지만 이 부분은 나중에 알아보자
# request 객체는 flask.wrappers.Request 클래스의 인스턴스이며, 이는 werkzeug.wrappers.RequestBase를 상속하고 있다

@app.route('/')
def index():
    return request.args['test_key']
    # Query Parameter는 werkzeug.wrappers.RequestBase의 프로퍼티인 'args'라는 MultiDict 객체에 접근해서 빼오면 된다
    # MultiDict는 werkzeug.datastructures.TypeConversionDict의 서브클래스이며
    # 이는 딕셔너리와 거의 동일하게 동작하지만 .get() 메소드에서 type conversion을 지원한다는 장점이 있다
    # request.args.to_dict()를 이용해 딕셔너리로 변환할 수도 있다

if __name__ == '__main__':
    app.run(debug=True)
