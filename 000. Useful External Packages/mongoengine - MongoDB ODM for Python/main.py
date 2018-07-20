# https://github.com/MongoEngine/mongoengine
# pip install mongoengine
from model import *
# RDB의 ORM 개념처럼, MongoDB와 같은 Document oriented NoSQL 데이터베이스는 ODM(Object-Document Mapping) 개념이 있다

# CRUD 중 C
user = User(id='city7310', pw='password', name='조민규').save()
# 클래스의 인스턴스를 얻어서 save()로 데이터 저장

# CRUD 중 R
# ClassName.objects로 데이터를 가져올 수 있고, 괄호 내에 조건을 명시할 수 있다
# 반환 데이터는 QuerySet인데 iterable하며 인덱싱 가능하고 list 캐스팅 가능하다
for u in User.objects(id='city7310'):
    # 각 요소는 모델 클래스의 인스턴스
    print(u.name)

data = User.objects()
print(type(data))
# 기본 상태는 QuerySet
print(type(list(data)))
# list 캐스팅 가능
print(list(data))
# User 객체들이 담겨 있음
print(list(data.as_pymongo()))
# as_pymongo()의 경우, value가 None인 key는 제거해 버리며 primary key는 _id로 바뀌므로 주의해야 한다
# 클래스에 명시해 둔 그대로 가져오고 싶다면, 각 object의 _data 필드에 접근하면 된다
print(data.first()._data)

print(type(data.first()))
# User 객체 하나에 접근(data.first() = data[0])
print(data.first().id)
# 속성에 접근
# MongoDB의 식별자는 명시적으로 _id지만, MongoEngine에서는 언더스코어 없이 id로 지정되어 있다
# _id로 접근하면 AttributeError를 raise하기도 한다

if User.objects(id='city7311'):
    # 검증
    print('city7311 already signed!')

print(User.objects.count())
# 카운팅. objects()와 objects 둘 다 가능하다

# CRUD 중 U
User.objects(id='city7310').first().update(name='새로운 민규')
print(User.objects().first().name)
# update 메소드를 쓰거나, 모델 객체의 데이터를 바꾸고 save()하는 방법도 있음

# CRUD 중 D
User.objects.delete()
# delete는 QuerySet에서만 가능함
