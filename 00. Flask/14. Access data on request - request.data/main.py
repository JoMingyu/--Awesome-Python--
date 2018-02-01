import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/json', methods=['POST'])
def json():
    # request.data는 Flask가 처리하지 못하는 content-type이 요청으로 오더라도 요청 데이터를 문자열 형태로 가져온다
    # request.data는 fallback으로 사용되기 때문에 대체적으로 비어 있다
    # body의 JSON 데이터를 가져오기 위해 request.data를 JSON parse하는 경우가 있는데, 그리 좋은 방법은 아니다

    req = json.loads(request.data)

    return str(req['test_key'])

app.run(debug=True)
