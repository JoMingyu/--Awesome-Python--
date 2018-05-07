# Flask는 텍스트를 처리할 때 유니코드를 사용한다
# 유니코드 처리를 클라이언트 측에서 해준다면 좋겠지만, 브라우저마다 달라서 서버에서 미리 처리해주는 편이 좋다
# wrappers.Response 클래스와 json 모듈의 도움을 받아 해결한다
import json

from flask import Flask, Response, jsonify

app = Flask(__name__)
resp = {'key': '한글한글'}


@app.route('/unicode')
def unicode():
    return jsonify(resp)


@app.route('/encoded')
def encoded():
    return Response(json.dumps(resp, ensure_ascii=False), content_type='application/json; charset=utf8')

# /unicode, /encoded 모두 웹브라우저로 접속해서 결과물을 보도록 하자
# - /unicode의 경우 한글 부분이 유니코드로 처리되고, /encoded의 경우 한글이 제대로 보인다
# 아래의 경우에는 jsonify와 다르게 헤더(application/json)를 따로 설정해야 한다는 것을 주의해야 한다

if __name__ == '__main__':
    app.run(debug=True)
