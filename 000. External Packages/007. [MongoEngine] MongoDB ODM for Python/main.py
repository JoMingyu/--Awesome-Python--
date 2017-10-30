# RDB의 ORM 개념처럼, MongoDB와 같은 Document oriented NoSQL 데이터베이스는 ODM을 지원한다
# pip install mongoengine

from model import *

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
# User 객체들의 list가 필요하지 않고, 즉시 데이터를 반환할 필요가 있다면 as_pymongo()의 리턴인 QuerySet에 list 캐스팅을 하자
print(list(data.as_pymongo()))
# as_pymongo()의 경우, value가 None인 key는 제거해 버리며 primary key는 _id로 바뀌므로 주의해야 한다
# as_pymongo()를 쓰지 않는 편이 오히려 코드가 간결해질 때가 많다
# 리스트를 돌며 필요없는 데이터들을 del하는 경우 자주 사용하게 되는데, objects의 반환에 Comprehension으로 필터링하는 편이 더 좋다

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

# CRUD 중 D
User.objects.delete()
# delete는 QuerySet에서만 가능함
