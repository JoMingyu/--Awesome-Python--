from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    # form-data의 value에 있는 json 데이터를 받아 보자
    req = request.form['json_data']
    print(type(req))
    # 역시 예상대로 문자열이다
    # 배워 뒀던 json 모듈을 사용하면 딕셔너리나 리스트로 바꿀 수 있다

    import json
    req_dict = json.loads(req)
    print(type(req_dict))
    # 성공적으로 dict가 됐다
    print(req_dict['test_key'])

    return ''


@app.route('/json', methods=['POST'])
def json():
    # 데이터 body 자체가 json인 요청은 request.json을 이용해서 받을 수 있다
    # 요청 헤더에서 반드시 Content-Type을 application/json으로 두어야 한다
    req = request.json
    print(type(req))
    # 자동으로 dict 또는 list로 캐스팅되어 들어온다

    return str(req['test_key'])

app.run(debug=True)
