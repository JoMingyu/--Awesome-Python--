from mongoengine import *

# MongoDB는 schemaless
# mongoengine을 이용해서 기존의 ORM 방식과 동일하게 document에 대한 스키마를 정의할 수 있음

connect('test_db')


class User(Document):
    # 클래스는 하나의 collection이 된다
    meta = {
        'collection': 'user'
    }
    # meta 필드를 사용해서 collection name을 직접 지정해둘 수 있다

    id = StringField(required=True, primary_key=True)
    # primary key 설정. 이 경우 document에서 ObjectId가 사라지고 이게 식별자가 된다
    # 따라서 primary key 속성 없이 'id'라는 이름을 가진 필드를 선언하지 말아야 한다. _id 또는 uid 등을 사용하는 편이 좋다
    # primary key가 어떻게 설정되어 있든 실제로 MongoDB 서버에 들어갈 땐 '_id'로 표기된다
    # MongoEngine에서 primary key에 접근하려면 MongoDB 표기 상의 _id는 신경쓰지 말고 primary key로 설정한 필드 이름 또는 'id'로 접근하면 된다
    # 이미 insert된 id가 다시 들어가더라도 오류는 생기지 않는데, 해당 값이 이미 있다면 update하기 때문이다

    pw = StringField(required=True)
    name = StringField(required=True, default='익명', max_length=10)
    # 테이블의 구조가 일반 ORM에서 정의되는 방식과 유사
    # 핵심적인 차이점은 MongoDB 자체에서 스키마가 적용되진 않는다는 것(어플리케이션 레벨에서만 적용되는 제약)
    # 필드의 default 값은 ListField와 DictField가 아닌 이상 None으로 처리됨
    # default가 callable하다면(함수나 클래스라면) document가 save될 때 호출하고, 반환값을 저장한다
    # -> default=datetime.now라면 save 시 해당 필드가 명시되지 않은 경우 해당 함수를 호출하여 필드에 적용


class Comment(EmbeddedDocument):
    # 먼저 댓글부터. 댓글은 일반적으로 하나의 게시물과 연관됨
    # MongoDB의 Embedded Document 개념을 사용하여 댓글을 Post document에 직접 포함된 document으로 저장할 수 있음
    # mongoengine을 사용하여 정규 document와 똑같은 방식으로 embedded document의 구조를 정의할 수 있음
    content = StringField()
    name = StringField(max_length=30)
    # Embedded Document는 별도로 명시해 주지 않으면 ID를 가지지 않는다는 것에 주의해야 함


class Post(Document):
    # 게시글이 Text, Image, Link post로 나뉜다고 생각해 보면 RDB의 경우 테이블을 따로 구조화시킬 것임
    # 이를 외래 키로 연결시키고, 다대다 관계를 제공하기 위해 링크 테이블도 필요하는 등 복잡함

    # MongoDB는 RDB가 아님 -> 결과적으로 schemaless 성질을 이용하여 해결할 수 있음
    # 모든 게시물을 하나의 컬렉션에 저장하고 각 게시물 유형은 필요한 필드만 추가해서 저장하면 됨
    # = 객체 지향의 상속 개념과 잘 어울림
    
    # 이 Post를 기본 클래스로, TextPost와 ImagePost, LinkPost를 Post의 하위 클래스로 생각할 수 있음
    # 메타에서 allow_inheriatnce를 True로 설정하여 상속 가능하도록 설계
    meta = {
        'abstract': True
        'allow_inheritance': True
    }

    title = StringField(max_length=10000, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    # 작성자는 User를 참조 : 전통적인 ORM의 외래 키 필드와 비슷함
    # 저장시 참조로 자동 변환되고, 로드될 때 참조 해제됨
    # 사용자가 삭제된 경우 모든 게시물을 삭제(reverse_delete_rule=CASCADE)
    # Circular import 문제를 해결하기 위해 문자열로 'User'를 넣어 주어도 됨

    tags = ListField(StringField(max_length=20))
    # Post는 공통적인 데이터 : 제목, 작성자, 태그만 다룸

    comments = EmbeddedDocumentListField(Comment)
    # 이 부분은 위쪽 Comment 클래스 참고


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    path = StringField()


class LinkPost(Post):
    url = StringField()
