from flask import Flask

app = Flask(__name__)


@app.route('/')
def json():
    # json response를 해보자
    # 파이썬은 사실 참 json같이 생긴 데이터 타입이 있다

    response = [{'name': 'planb', 'age': 18}, {'name': 'jgc', 'age': 18}]
    # list는 json array에, dictionary는 json object에 대응된다

    # 하지만 아래의 단순한 구문은 response에 성공하지 않는다
    # return response
    # TypeError: 'list' object is not callable

    # json 모듈을 사용할 수 있는데, json 데이터가 한 line에 쭉 리턴되기 때문에 보기 조금 불편하다
    # flask의 jsonify를 사용하면 indent 적용된 예쁜 json 데이터를 응답할 수 있다
    from flask import jsonify

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
