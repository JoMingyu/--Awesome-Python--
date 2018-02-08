from flask import Flask, request

app = Flask(__name__)


@app.route('/json', methods=['POST'])
def json():
    # 요청의 Content-Type이 application/json이고, 직렬화된 JSON 문자열이 들어온다면(표준에 아주 잘~맞는 JSON request라면)
    # request의 json property나 get_json() 메소드를 이용하면 된다
    # Flask 0.10에서 get_json() 메소드가 추가되었는데, 이 메소드를 이용하는 편이 더 좋다
    # https://stackoverflow.com/a/20001283
    
    req = request.json
    req = request.get_json()
    # 요청의 Content-Type이 application/json이 아니라면 None으로 처리되며
    # Content-Type은 application/json으로 설정되었으나 아무 데이터도 전달되지 않으면 status code 400을 지동으로 리턴한다

    # 요청의 타입이 json인지 확인해 주는 메소드도 있다
    if not request.is_json:
        return 'Please set your content type "application/json"!', 400
    
    print(type(req))
    # json 프로퍼티는 요청 데이터에 따라 파이썬 고유의 dict 또는 list 타입으로 처리된다

    return str(req['test_key'])

app.run(debug=True)
