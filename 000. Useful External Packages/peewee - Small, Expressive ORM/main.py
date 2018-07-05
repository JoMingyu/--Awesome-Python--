# https://github.com/coleifer/peewee
# pip install peewee
from peewee import *
# SQLite, MySQL, PostgreSQL을 지원하는 간단하고 표현이 풍부한 API를 가진 ORM
# 개인적으로 SQLAlchemy보다 선호한다

db = MySQLDatabase('test', user='root')
# SQLiteDatabase, MySQLDatabase, PostgreSQLDatabase 클래스를 지원
# 내부적으로는 각 데이터베이스의 driver를 통해 데이터베이스에 연결하므로, 아래의 코드 블럭을 참고하면 도움이 될 것이다
# https://github.com/coleifer/peewee/blob/master/peewee.py#L24-L57

from datetime import datetime

class User(Model):
    # 각 모델은 Model 클래스를 상속받아 정의
    signup_time = DateTimeField(default=datetime.now)

    id = CharField(primary_key=True)
    # 모든 필드 클래스들은 Field를 상속받고 있으며, 따라서 필드 정의 시 필요한 속성은 Field 클래스의 생성자를 참고하도록 하자
    # https://github.com/coleifer/peewee/blob/master/peewee.py#L3722
    
    pw = CharField()

    class Meta:
        database = db
        # 모든 모델 클래스는 inner class로 database 필드를 가진 'Meta' 클래스를 정의하고 있어야 한다


class Pet(Model):
    owner = ForeignKeyField(User, null=True)
    # Foreign key

    name = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables((User, Pet))

# --- Create

planb = User.create(id='planb', pw='pass')
# Model.create()를 통해 모델 인스턴스를 생성할 수 있음
# 새로운 인스턴스가 반환되고 테이블에 row가 생성

query = User.insert(id='planb2', pw='pass')
query.execute()
# 모델 인스턴스 반환이 필요없고, 간단한 insert만 필요한 경우

# --- Retrieve

query = User.select()
users = query.execute()
print(users[0])
# 'planb'
# 모델 인스턴스의 __repr__은 해당 스키마의 primary key를 반환함

query = User.select()
print(query[0])
# 'planb'
# query 객체에 즉시 접근하면, execute()의 실행 결과를 반환한다
# SQLAlchemy도 위와 같은 표현이 가능한 것으로 보아 파이썬 ORM 라이브러리 종특인 것 같다

query = User.select().where(User.id == 'planb2')
user = query.get()
# execute()는 list를 반환하고, get()은 결과의 첫 row에 해당하는 모델 인스턴스를 반환
print(user)
# 'planb2'

# --- Update

query = User.update(pw='new_pw').where(User.id == 'planb')
query.execute()

print(User.select().where(User.id == 'planb').execute()[0].pw)
# 'new_pw'

# --- Delete

query = User.delete()
query.execute()