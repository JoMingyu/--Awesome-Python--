# https://github.com/mongodb/mongo-python-driver
# pip install pymongo
import pymongo
from pymongo import MongoClient
# MongoDB 서버에 접근하기 위한 모듈
# 당연한 이야기지만 MongoClient로 접근하려면 MongoDB Server나 docker를 통해 MongoDB 서버를 실행시켜 주어야 한다

collection = None


def initialize():
    client = MongoClient('localhost', 27017)
    # = MongoClient('mongodb://localhost:27017/')
    # 클래스의 생성자 자체는 host와 port를 None으로 두고 있으나, 생성자 내부 코드에서 localhost와 27017을 기본으로 세팅해 준다

    db = client.test_db
    # test_db라는 이름을 가진 데이터베이스
    # 없으면 만든다

    global collection
    collection = db.test_coll
    # test_coll이라는 이름을 가진 컬렉션
    # 데이터베이스 때처럼 컬렉션도 없으면 만든다

initialize()


def insert_sample():
    print('------ insert sample')
    data = {
        'title': 'titletitlte',
        'content': 'foo',
        'author': 'PlanB'
    }
    # document가 될 데이터(딕셔너리)

    print(f'Insert : {collection.insert(data)}')
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
    print(f'Insert list : {collection.insert(data)}')
    # id는 통째로 넣는 list의 갯수만큼 list로 반환된다


def find_sample():
    print('------ find sample')
    # 이제 도큐먼트를 찾아 보도록 하자
    found_datas = collection.find()

    print(f'Result of find : {found_datas}')
    # Cursor가 반환된다. iterable하기 때문에 걍 for문 돌리면 된다

    # for data in found_datas:
    #     print(data)

    # find 시 반환되는 Cursor 객체는 같은 iterable 객체인 list로 캐스팅 가능하다
    print(f'Cast to list : {list(found_datas)}')

    # 하나만 가져와 보자
    # find_one의 반환값은 기본적으로 딕셔너리다
    print(f"Find one : {collection.find_one()}")

    # 데이터의 length가 궁금할 때도 있다.
    print(f'Data length : {found_datas.count()}')

    # 결과에 제한을 걸 수도 있다. SQL의 WHERE 문과 비슷하다
    print(f'Sample of author is JGC : {list(collection.find({"author": "JGC"}))}')

    # 이 데이터에 들어 있는 _id의 값(ObjectId)은 직렬화 불가능하다. 필요없으면 빼도록 하자
    print(f'Remove _id : {list(collection.find({}, {"_id": False}))}')

    # sort해 보자
    print(f"Sort by title : {list(collection.find().sort('title', pymongo.ASCENDING))}")
    # sort(key_name, sort_type)


def update_sample():
    print('------ update sample')
    print(collection.update({'title': 'Yes!!'}, {'title': 'New!', 'author': 'JGC'}))
    # 기존에 있던 데이터가 제거되고 뒤쪽의 딕셔너리가 들어간다. 기존엔 title, content, author로 이루어져 있었지만 이 명령이 수행되고 나면 content는 사라진다
    # ObjectId는 손실되지 않는다
    # 조건에 대한 데이터가 없다면(이 경우 title이 'Yes!!'인 데이터) 명령 자체는 성공하지만 결과적으로 바뀌는 데이터는 없다


def remove_sample():
    print('------ remove sample')
    print(f'Before remove : {list(collection.find())}')
    collection.remove({'author': 'JGC'})
    print(f'After remove : {list(collection.find())}')
    collection.remove()

insert_sample()
find_sample()
update_sample()
find_sample()
remove_sample()
