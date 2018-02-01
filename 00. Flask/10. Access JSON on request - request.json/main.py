from flask import Flask, request

app = Flask(__name__)


@app.route('/json', methods=['POST'])
def json():
    # 요청의 Content-Type이 application/json이고, 직렬화된 JSON 문자열이 들어온다면(아주 정상적인 JSON request라면)
    # request의 json property나 get_json() 메소드를 이용하면 된다
    # Flask 0.10에서 get_json() 메소드가 추가되었는데, 이 메소드를 이용하는 편이 더 좋다
    # https://stackoverflow.com/a/20001283

    # 요청의 Content-Type이 application/json이 아니라면 데이터를 받아들이지 못한다
    req = request.json
    print(type(req))
    # json 프로퍼티는 파이썬 고유의 dict 또는 list 타입으로 되어 있다

    return str(req['test_key'])

app.run(debug=True)
