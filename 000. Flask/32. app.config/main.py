from flask import Flask

app = Flask(__name__)

app.config['CONFIG'] = 'hello?'
# app의 config를 통해 설정 값들을 저장할 수 있다
# config를 계속 따라가다 보면, Flask에서 dict를 상속받은 클래스를 통해 config를 만들어내는 걸 볼 수 있다

print(app.config['CONFIG'])

app.config['SECRET_KEY'] = 'qwe'
# config의 유명한 속성 중 하나는 이 secret key다. 타 패키지들이 자주 참조한다
print(app.secret_key)
# 이 secret key는 app 객체의 secret_key 필드로도 참조 가능하다
# Flask의 세션에서 시큐어 쿠키를 구현하기 위한 key가 될 때도 있고
# Flask-JWT에서 authenticate 함수의 JWT 토큰 암호화를 위한 key가 될 때도 있다

# Flask에 능숙한 파이썬 백엔드 개발자들은 이 config를 능숙하게 사용한다
