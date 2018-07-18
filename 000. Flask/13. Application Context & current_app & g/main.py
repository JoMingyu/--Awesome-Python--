# http://flask.pocoo.org/docs/1.0/appcontext/
# Application context는 요청을 처리하는 동안 어플리케이션 레벨의 데이터를 관리하기 위해 사용한다
# context는 같은 전역 변수지만 실제 내용은 각 요청(문맥)마다 다른 것을 가르키게 만들어둔 것이다
# 그렇게 만든 이유 : http://flask.pocoo.org/docs/1.0/design/#thread-locals
# Application context에 해당하는 대표적인 객체로, current_app과 g가 있다

# Flask 객체는 config와 같은 속성들을 가지고 있다. 그러나, 단순히 해당 객체를 import하는 것은 circular import(서로 다른 모듈에서 서로 import) 문제를 일으킬 수 있다
# Flask는 이러한 문제를 application context라는 개념을 이용해 극복했고, Flask 객체를 직접 참조하지 않고 current_app을 사용하도록 지원한다
from flask import Flask, current_app

app = Flask(__name__)
app.config['SOME'] = True


@app.route('/')
def index():
    # 요청을 처리할 때, Flask는 자동으로 application context를 push한다. view function, error handler 등 요청 중에 실행되는 것들은 current_app에 액세스할 수 있다
    return 'Config SOME is {}'.format(current_app.config['SOME'])

# current_app은 view function처럼 요청 중에 실행되는 기능에서 사용하는 게 아니라면 RuntimeError가 raise되는데, 이를 해결하기 위해 수동으로 context를 push할 수도 있다
with app.app_context():
    # [app.Flask]
    #     def app_context(self)
    # 해당 메소드는 app.ctx.AppContext 객체를 반환하며, 해당 클래스에는 __enter__와 __exit__이 정의되어 있어 비교적 깔끔한 with 문을 사용할 수 있다
    print(current_app.config['SOME'])


from flask import g
# Application context는 요청을 처리하는 동안에만 사용할 데이터를 저장하기 좋은 장소다
# 이를 위해 Flask는 g라는 객체를 제공(global의 약자)하며, 이는 어떤 속성이든 자유롭게 정의할 수 있는 간단한 namespace이다
# 이는 Request context에서 유용하니, 해당 순서에서 알아보도록 하자

if __name__ == '__main__':
    app.run(debug=True)