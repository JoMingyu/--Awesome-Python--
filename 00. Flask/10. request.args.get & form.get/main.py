from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    # 원래 우리가 요청 데이터에 접근하게 사용했던 방법은 아래와 같았다
    print(request.form['test_key'])

    # 만약 value를 int형으로 받아야 한다면, 아래처럼 캐스팅을 해야할 것이다
    value = int(request.form['test_key'])
    print(value)

    # key가 없을 때 기본값 0을 가져야 한다면?
    value = 0 if 'test_key' not in request.form else int(request.form['test_key'])
    # 코드가 너무 길어진다. werkzeug.datastructures.TypeConversionDict에는 .get 메소드에서 type conversion을 지원한다고 했다
    # request.args, request.form 둘 다 TypeConversionDict의 서브클래스인 MultiDict의 인스턴스이므로 써먹어볼 수 있다

    value = request.form.get('test_key2', 0, int)
    value = request.form.get('test_key', type=int)
    # 딕셔너리가 기본적으로 지원하는 기본값 처리에, 추가적으로 캐스팅을 도와준다.
    # get('test_key2')만 쓸수도 있다
    # 위처럼 기본값 처리와 캐스팅에 도움을 받기 위해 get()을 사용하곤 한다

    print(value)
    print(type(value))

    return ''

if __name__ == '__main__':
    app.run(debug=True)
