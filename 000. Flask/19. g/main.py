from flask import Flask, g
# flask의 글로벌 객체 g
from another_module import access_g

app = Flask(__name__)


@app.route('/')
def index():
    # application context 밖에서 g를 컨트롤하면 RuntimeError가 발생한다
    # RuntimeError: Working outside of application context.
    g.any_data = 'qweqwe'
    access_g()

    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
