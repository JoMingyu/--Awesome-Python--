from flask import Flask, request

# https://github.com/lepture/flask-wtf
# pip install flask-wtf
from wtforms import *
# 요청에 대한 폼 유효성을 검증하기 위한 패키지

app = Flask(__name__)


class SignupForm(Form):
    # 각 필드가 form의 key가 되고, wtforms.validators를 이용해 validation해줄 수 있다
    id = TextField('ID', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    name = TextField('Name', [validators.Length(max=10)])


@app.route('/signup', methods=['POST'])
def singup():
    print(request.form)
    form = SignupForm(request.form)

    if form.validate():
        return 'hello!', 201
    else:
        return 'sorry!', 400


app.run(debug=True)
