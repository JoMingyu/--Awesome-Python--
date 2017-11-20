from flask import Flask

app = Flask(__name__)


@app.route('/')
def json():
    # json response를 해보자
    # 파이썬에는 json과 대응되는 데이터 타입이 있다

    data = [{'name': 'planb', 'age': 18}, {'name': 'jgc', 'age': 18}]
    # list는 json array에, dictionary는 json object에 대응된다

    # 하지만 아래의 단순한 구문은 response에 성공하지 않는다
    # return data
    # TypeError: 'list' object is not callable
    
    # json response를 위해 대표적으로 3가지 방법을 사용할 수 있다
    # 1. return str(data)
    # 2. return json.dumps(data)
    # 위의 두 경우는 Content Type이 text/html이기 때문에 필요에 따라 따로 헤더를 적용해줘야 하는 등의 번거로움이 있다

    # flask의 jsonify는 flask.wrappers.Response의 객체를 반환한다
    # Content Type이 application/json으로 설정되고, 반환 데이터도 문자열 처리된다
    from flask import jsonify

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
