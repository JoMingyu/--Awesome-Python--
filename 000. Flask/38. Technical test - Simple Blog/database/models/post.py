from database.mongodb import *
from database.models.user import User
from datetime import date


class Comment(EmbeddedDocument):
    content = StringField(required=True)
    author = ReferenceField(User, required=True)


class Post(Document):
    title = StringField(required=True, max_length=300)
    content = StringField(required=True, max_length=5000)
    author = ReferenceField(User, required=True)
    post_date = StringField(required=True, default=str(date.today()))
    comments = EmbeddedDocumentListField(Comment)
