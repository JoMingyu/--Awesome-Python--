# https://github.com/zzzeek/sqlalchemy
# pip install sqlalchemy
from sqlalchemy import create_engine
# 관계형 데이터베이스의 '테이블'과 '컬럼' 개념은 OOP 언어의 '클래스'와 '프로퍼티'와 대응시킬 가능성이 다분하다
# 실제로 OOP의 객체(Object)와 관계형 데이터베이스의 관계(Relation)을 연관(Mapping)짓기 위하여 개발이 진행되었고
# 이후 ORM(Object Relational Mapping)이라는 개념이 등장, SQLAlchemy와 같은 Object Relational Mapper가 개발되었다
# ORM을 사용하면, 테이블과 코드 각각을 따로 관리하지 않아도 되고, 쿼리와 raw data 대신 메소드와 객체로 데이터를 컨트롤할 수 있어 편하다
# SQLAlchemy를 비롯한 ORM 라이브러리들은 대부분 쿼리 객체를 얻어온 후 이를 execute하는 방식을 사용한다

engine = create_engine('mysql+pymysql://root@localhost/test')
# sqlalchemy는 데이터베이스 접근 클라이언트에 engine이라는 어휘를 사용한다
# 위는 MySQL 데이터베이스의 URL을 이용해 engine 객체를 만드는 statement이며
# 각 데이터베이스들의 URL 샘플은 SQLAlchemy docs - Engine Configuration에서 확인할 수 있다
# http://docs.sqlalchemy.org/en/latest/core/engines.html

print(engine.execute('select 1').scalar())
# 1
# engine은 선언 당시가 아니라, 쿼리 첫 실행 시 데이터베이스에 연결된다
# 위처럼 engine을 직접 이용해 쿼리할 수도 있고, ORM 모델 클래스를 선언하여 사용할 수도 있다(권장되며 SQLAlchemy같은 mapper를 사용하는 이유)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# ORM 모델 클래스를 만드려면, declarative_base라는 함수를 사용해 Base 클래스를 먼저 가져와 주어야 한다

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class User(Base):
    __tablename__ = 'tbl_users'

    signup_time = Column(DateTime, default=datetime.now)
    id = Column(String(50), primary_key=True)
    # String(MySQL 기준 Varchar), 최대 길이는 50, primary key
    pw = Column(String(50))

    def __init__(self, id, pw):
        self.id = id
        self.pw = pw

# 위의 클래스는 테이블 생성이 되지 않은 상태인데, Base를 통해 쉽게 생성할 수 있다
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
# ORM이 데이터베이스를 조작하는 방법은 session인데, sqlalchemy.orm.sessionmaker로 session 객체를 얻어올 수 있다

session = Session()
# 모든 쿼리의 첫걸음이 될 객체

# --- Create

session.add(User('PlanB', 'password'))
# 사용자 객체 추가
session.add_all([
    User('PlanB2', 'password'),
    User('Flouie', 'pasSword')
])
# 여러 개를 한꺼번에 추가
session.commit()
# commit

# --- Retrieve

query = session.query(User)
# session의 query 메소드를 사용하면 Query 객체가 나오는데, 이를 통해 SQL처럼 filtering이나 ordering 쿼리 등을 수행할 수 있다

query = query.filter(User.id.in_(['PlanB', 'PlanB2']))
# 위는 query()로 얻어온 Query 객체에, id가 'PlanB'나 'PlanB2'에 속하는 row만 필터링되도록 한 새로운 Query 객체를 가져오는 statement
# filter 방식은 여러 종류가 있는데, 일반적으로 [Obj].[Field].[Method]()같은 방식으로 수행한다
# filter(User.id.like('Plan%')), filter(User.id == 'PlanB') 등. 아래 링크에 잘 설명되어 있다
# http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators

res = session.query(User).get('PlanB')
# get()은 Primary key를 통한 조회
# 해당 값에 대한 row가 있으면 객체를 반환하고, 없으면 None을 반환

res = query.all()
# query 객체의 all() 메소드는 해당 쿼리를 수행한 결과의 모든 row를 가져온다
# 가장 첫 row에 해당하는 객체를 가져오거나, 없으면 None을 반환하는 first()
# 결과가 단 하나만 있는 경우 해당 객체를 반환하고, 결과가 없거나 여러 개가 있으면 에러를 raise하는 one()
# one()을 실행하고, 성공하면 첫 컬럼의 데이터를 반환하는 scalar()
# 쿼리 결과의 수(COUNT(*))를 반환하는 count() 등이 있다

print(res)
# [<__main__.User object at 0x10a7b4a58>, <__main__.User object at 0x10a7b4ac8>]
print(res[0].pw)
# 'password'
# Query 객체는 list-like해서 위처럼 인덱싱 가능하며, 슬라이싱도 지원한다

res = session.query(User).filter(User.id == 'PlanB').filter(User.pw == 'password').all()
# id가 'PlanB', password가 'password'인 row만 필터링

for signup_time, id in session.query(User.signup_time, User.id).all():
    # 특정 column 데이터만 가져오기
    print(signup_time, id)

# --- Delete

users = session.query(User).delete()
# 쿼리해서 가져온 후, delete
session.commit()