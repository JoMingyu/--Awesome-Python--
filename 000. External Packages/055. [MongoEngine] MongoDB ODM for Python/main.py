from model import *

# CRUD 중 C
user = User(uid='city7310', pw='password', name='조민규').save()
# 클래스의 인스턴스를 얻어서 save()로 데이터 저장

# CRUD 중 R
# ClassName.objects로 데이터를 가져올 수 있고, 괄호 내에 조건을 명시할 수 있다
# 반환 데이터는 QuerySet인데 iterable하며 인덱싱 가능하고 list 캐스팅 가능하다
for u in User.objects(uid='city7310'):
    # 각 요소는 모델 클래스의 인스턴스
    print(u.name)

data = User.objects()
print(type(data))
# 기본 상태는 QuerySet
print(type(list(data)))
# list 캐스팅 가능
print(list(data))
# User 객체들이 담겨 있음

print(type(data.first()))
# User 객체 하나에 접근(data.first() = data[0])
print(data.first().uid)
print(data.first().id)
# 속성에 접근
# MongoDB의 식별자는 명시적으로 _id지만, MongoEngine에서는 언더스코어 없이 id로 지정되어 있다
# _id로 접근하면 AttributeError를 raise하기도 한다

if User.objects(uid='city7311'):
    # 검증
    print('city7311 already signed!')

print(User.objects.count())
# 카운팅

# CRUD 중 U
User.objects(uid='city7310').update(name='새로운 민규')
print(User.objects().first().name)

# CRUD 중 D
User.objects().delete()
# delete는 QuerySet에서만 가능함
