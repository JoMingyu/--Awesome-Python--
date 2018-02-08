from flask import Flask

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
# app에는 logger라는 property가 있다
print(app.logger)
# logger에는 handler를 달아줘야 하는데, 이를 위해서 RotatingFileHandler를 import했다


@app.before_first_request
# 첫번째 요청 이전에 logger를 세팅하도록 했다
def before_first_request():
    def make_logger():
        handler = RotatingFileHandler('server_log.log', maxBytes=100000, backupCount=5)
        # 먼저 해야할 건 RotatingFileHandler 클래스를 통해 핸들러(인스턴스)를 얻어내는 일

        formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
        # 로그 포매팅을 위해 logging 모듈의 Formatter 클래스를 사용한다

        handler.setFormatter(formatter)
        # 핸들러에 포매터를 달아 준다

        app.logger.addHandler(handler)
        # app의 logger propery에 핸들러를 추가시킨다

        app.logger.setLevel(logging.INFO)
        # logger의 level을 세팅해 준다.(어떤 단계 이상의 로그를 기록할지)
        # 기본 level은 WARNING이다

    make_logger()

    print(app.logger)

    app.logger.info('------ Logger started ------')


@app.route('/')
def index():
    app.logger.info('Access index!')
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
