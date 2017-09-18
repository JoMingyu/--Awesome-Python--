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

    # request의 Json 데이터를 받았던 것처럼 json 모듈을 쓰면 된다
    import json

    return json.dumps(response)

app.run(debug=True)
