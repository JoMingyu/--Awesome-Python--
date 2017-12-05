# 대부분의 사람들은 데이터베이스에 접근하기 위해 SQLAlchemy를 선호한다(ORM을 위해)
# 이런 경우 Flask 어플리케이션은 모듈보다는 패키지를 사용하며, 모델들은 분리된 모듈로 만드는 것이 좋다
# SQLAlchemy를 사용하는 4가지 방식이 있다

# 1. Flask-SQLAlchemy
# 2. 선언형(Declarative)
# 3. 수동 ORM
# 4. SQL 추상 계층

# SQLAlchemy는  공통 데이터베이스 추상 계층이고, 따라서 설정하는 데에 약간의 노력을 요하는 매퍼이기 때문에
# Flask에서 SQLAlchemy를 사용할 것이라면 Flask의 SQLAlchemy 확장(Flask-SQLAlchemy)를 사용하는 것이 편하고 유연함

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# pip install flask-sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/dmdkz/test.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    pw = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    # Unresolved attribute reference warning이 뜨지만, 무시하고 진행하자


User.query.delete()
# delete

db.session.add(User(id='1234', pw='1234', phone='01012345678'))
db.session.add(User(id='123', pw='123', phone='01087654321'))
db.session.commit()
# insert

# --- select
print(User.query)
# 쿼리문 자체

print(User.query.all())
# 전체 Select(list 타입)
print(User.query.first())
# First Select(User 타입)

print(User.query.filter_by(id='1234').all())
# Filtered Select(list 타입)
print(User.query.filter_by(id='1234').first())
# First Select(User 타입)

print(User.query.get('123'))
# Primary Key를 통한 select

print(User.query.order_by(User.id).all())
# Ordering

user = User.query.get('123')
user.pw = 'new'
db.session.commit()
# update
print(User.query.get('123').pw)
