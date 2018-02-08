from flask import Flask
# pip install flask-mongoengine
from flask_mongoengine import MongoEngine
# MongoEngine의 Flask Extension
# Document로 선언된 모델을 WTForms 형태로 변환할 수 있는 부분이 강점
# https://flask-mongoengine.readthedocs.io/en/latest/


db = MongoEngine()
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'localhost',
    'port': 27017
    # default 27017
}
db.init_app(app)


class User(db.Document):
    id = db.StringField(primary_key=True)
    pw = db.StringField(required=True)
    phone = db.StringField(max_length=20, required=True, unique=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.id, self.pw, self.phone)

User.objects.delete()
# delete

User(id='123', pw='123', phone='01012345678').save()
# insert

print(User.objects.first())
# select

user = User.objects.first()
user.pw = 'new'
user.save()
# update

print(User.objects(pw='new').first())
# filtered select
