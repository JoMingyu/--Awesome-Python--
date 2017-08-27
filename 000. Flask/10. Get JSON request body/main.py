from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def index():
    # body에 있는 json 데이터를 받아 보자
    req = request.form['json_data']
    print(type(req))
    # 역시 예상대로 문자열이다
    # 배워 뒀던 json 모듈을 사용하면 딕셔너리나 리스트로 바꿀 수 있다

    import json
    req_dict = json.loads(req)
    print(type(req_dict))
    # 성공적으로 dict가 됐다
    print(req_dict['key'])

    return ''

app.run(debug=True)
