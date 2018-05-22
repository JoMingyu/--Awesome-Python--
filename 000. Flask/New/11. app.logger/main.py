from flask import Flask

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
# Flask 객체에는 logger라는 property가 있으며, 이는 Python의 빌트인 모듈인 logging에서 생성된 표준 logger를 사용
print(app.logger)
# Flask.logger는 'flask.app'이라는 이름의 logger를 반환
# 여기에 custom logger를 붙여줄 수 있다


def make_logger():
    handler = RotatingFileHandler('server_log.log', maxBytes=100000, backupCount=5)
    # 1. RotatingFileHandler 클래스를 통해 handler 객체를 얻고

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
    # 2. logging.Formatter를 사용하여 로그 포매팅

    handler.setFormatter(formatter)
    # 3. 핸들러에 setFormatter

    app.logger.addHandler(handler)
    # 4. app의 logger propery에 핸들러를 추가

    app.logger.setLevel(logging.INFO)
    # 5. logger의 level을 세팅(어떤 단계 이상의 로그를 기록할지)
    # -> 기본 level은 WARNING

make_logger()

print(app.logger)

app.logger.info('------ Logger started ------')


@app.route('/')
def index():
    app.logger.info('Access index!')
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
