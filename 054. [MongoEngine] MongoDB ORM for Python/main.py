from model import *

# CRUD 중 C
user = User(uid='city7310', pw='password', name='조민규').save()
# 클래스의 인스턴스를 얻어서 save()로 데이터 저장

# CRUD 중 R
# ClassName.objects로 데이터를 가져올 수 있고, 괄호 내에 조건을 명시할 수 있다
# 반환 데이터는 QuerySet인데 iterable하며 인덱싱 가능하다
for u in User.objects(uid='city7310'):
    # 각 요소는 모델 클래스의 인스턴스
    print(u.name)

if User.objects(uid='city7311'):
    # 검증
    print('city7311 already signed!')

print(User.objects().count())
# 카운팅

# CRUD 중 U
User.objects(uid='city7310').update(name='새로운 민규')
# 업데이트
print(User.objects().first().name)
# User.objects().first = User.objects()[0]

# CRUD 중 D
User.objects().delete()
# 삭제
# delete는 QuerySet에서 가능함
