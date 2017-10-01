from database.models.user import User


class UserModel:
    # Document를 상속받은 User 클래스에서 id 속성을 다루면 MongoDB의 ObjectId가 들어가므로
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw


def authenticate(id, pw):
    if id and pw and User.objects(id=id, pw=pw):
        return UserModel(id=id, pw=pw)


def identity(payload):
    return payload['identity']
