from database.mongodb import *


class User(Document):
    id = StringField(required=True, primary_key=True)
    pw = StringField(required=True)
