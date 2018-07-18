from flask import Flask, request

app = Flask(__name__)


@app.route('/json', methods=['POST'])
def json():
    # 요청의 Content-Type이 application/json이고, 직렬화된 JSON 문자열이 들어온다면(RFC 표준에 잘 맞는 JSON request라면)
    # request의 json property나 get_json() 메소드를 이용하면 된다
    
    req = request.json
    # Flask 0.12.3까지 deprecated되어 있었으나, Flask 1.0에선 다시 deprecated가 제거됨

    req = request.get_json()
    # Flask 0.10에서 추가된 메소드

    # 요청의 Content-Type이 application/json이 아니라면 None이 반환되며
    # Content-Type은 application/json으로 설정되었으나 아무 데이터도 전달되지 않으면 status code '400 Bad Request'를 지동으로 리턴한다

    # 요청의 타입이 json인지 확인해 주는 메소드도 있다
    if not request.is_json:
        return 'Please set your content type "application/json"!', 400
    
    print(type(req))
    # json 프로퍼티는 요청 데이터에 따라 파이썬 고유의 dict 또는 list 타입으로 처리된다

    return str(req['test_key'])

if __name__ == '__main__':
    app.run(debug=True)
