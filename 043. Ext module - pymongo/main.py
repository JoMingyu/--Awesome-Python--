# pip install pymongo
# [MongoDB download page]
# https://www.mongodb.com/dr/fastdl.mongodb.org/win32/mongodb-win32-x86_64-2008plus-ssl-3.4.7-signed.msi/download

# 당연한 이야기지만 MongoClient로 접근하려면 mongod를 통해 mongodb 서버를 실행시켜 주어야 한다
# MongoDB는 Server -> database -> collection -> document 순서로 작아지는 개념이다

import pymongo
from pymongo import MongoClient
# MongoDB 서버에 접근하기 위한 모듈

collection = None


def initialize():
    client = MongoClient('localhost', 27017)
    # = MongoClient('mongodb://localhost:27017/')

    db = client.test_db
    # test_db라는 이름을 가진 데이터베이스
    # 없으면 만든다

    global collection
    collection = db.test_coll
    # test_coll이라는 이름을 가진 컬렉션
    # 데이터베이스 때처럼 컬렉션도 없으면 만든다

initialize()


def insert_sample():
    data = {
        'title': 'titletitlte',
        'content': 'foo',
        'author': 'PlanB'
    }
    # document가 될 데이터(딕셔너리)

    print(collection.insert(data))
    # 컬렉션에 대해 도큐먼트를 insert
    # 데이터가 _id 키를 가지고 있지 않으면 MongoDB가 알아서 도큐먼트에 유니크한 _id 키를 부여해서 insert

    # 통째로 insert할 수도 있다. list에 dictionary를 끼워넣자
    data = [
        {
            'title': 'titletitlte',
            'content': 'foo',
            'author': 'PlanB'
        },
        {
            'title': 'Yes!!',
            'content': "I'm Javascript king",
            'author': 'JGC'
        }
    ]
    print(collection.insert(data))
    # id는 통째로 넣는 list의 갯수만큼 list로 반환된다

insert_sample()


def find_sample():
    # 이제 도큐먼트를 찾아 보도록 하자
    found_datas = collection.find()
    print('Result of find :', found_datas)
    # Cursor가 반환된다. iterable하기 때문에 걍 for문 돌리면 된다

    for data in found_datas:
        print(data)

    # 이 Cursor 객체는 같은 iterable 객체인 list로 캐스팅 가능하다
    print(list(data))

    # 데이터의 length가 궁금할 때도 있다.
    print(found_datas.count())

    print('----------------------------------------------')
    # 결과에 제한을 걸 수도 있다. SQL의 WHERE 문과 비슷하다
    print(list(collection.find({'author': 'JGC'})))

    # 이 데이터에 들어 있는 _id의 값(ObjectId)은 직렬화 불가능하다. 필요없으면 빼도록 하자
    print(list(collection.find({}, {'_id': False})))

    # sort해 보자
    print(list(collection.find().sort('title', pymongo.ASCENDING)))
    # sort(key_name, sort_type

find_sample()
