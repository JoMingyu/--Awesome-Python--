from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    if 'test_key' in request.args:
        return '', 200
    else:
        return '', 204


if __name__ == '__main__':
    app.run(debug=True)
