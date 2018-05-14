from flask import Flask

# https://github.com/alisaifee/flask-limiter
# pip install flask-flimite
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
# flask 어플리케이션이나 특정 endpoint에 대한 요청 수 제한 기능을 제공
# 제공하는 OpenAPI에 '하루 최대 1000개 요청'과 같은 조건을 걸 때 유용하게 사용할 수 있음

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    # Limit의 대상이 될 key function
    # 요청마다 key function을 호출하며, 해당 함수가 반환하는 값에 요청을 count, limit보다 많아지면 429를 abort하는 구조
    # 여기서는 특정 호스트에 대해 limiting하도록 요청의 IP(request.remote_addr)를 반환하는 flask_limiter.util.get_remote_address를 key_func로 둠
    default_limits=['100000 per 7days', '20000 per day', '2000 per hour', '50/minute', '2/second']
    # 일주일에 100000, 하루에 20000, 1시간에 2000, 1분에 50, 1초에 2 request를 한계치로 둠
    # [max_request_num] per [period] 또는 [max_request_num]/[period]
)


@app.route('/slow')
@limiter.limit('10/minute')
# 특정 view function에 대해서 limit을 걸 수도 있음. 여기서는 1분에 10 request를 한계치로
def slow():
    return 'slow'
    # 한계치보다 많은 request가 들어올 경우, 429 Too Many Requests를 반환


@app.route('/too-slow')
@limiter.limit('200/hour')
@limiter.limit('5/minute')
# 여러 개의 limit을 주는 경우
# '200/hour;5/minute'처럼 세미콜론으로 분할해도 됨
def too_slow():
    return 'too slow'


@app.route('/common')
def common():
    return 'common'


@app.route('/exempt')
@limiter.exempt
# limiter에서 제외
def exempt():
    return 'exempt'


if __name__ == '__main__':
    app.run(debug=True)
