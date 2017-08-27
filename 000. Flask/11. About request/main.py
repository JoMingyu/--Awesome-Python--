from flask import Flask, request

app = Flask(__name__)


# request 객체에선 가져올 수 있는 속성이 정말 많다
@app.route('/')
def index():
    print(request)
    print(request.path)
    print(request.method)
    print(request.host)
    # 또 request parameter를 위한 args, body data를 위한 form, files 등이 있다
    
    return 'hello'

app.run(debug=True)
