# 언더스코어는 private을 표현하기 위해서도 사용된다
# 대표적인 방어적 프로그래밍 언어인 Java의 경우 키워드로서 private와 같은 접근 제한자를 제공하나,
# Python은 문법적으로 캡슐화를 지원하지 않으며, 관례적으로 '접근하지 말라'라는 의미로 요소 이름 앞에 언더스코어를 붙인다
# 이는 진정한 의미의 private은 아니며 단순히 권고사항일 뿐이므로 실제로 접근하면 warning 정도만 발생하고,
# 해당 접근에 대한 책임은 접근자 자신에게 있다

_n = 3

# 언더스코어를 통한 private 표현은 클래스에서 property를 사용할 때 자주 쓰인다
class User:
    def __init__(self, id, pw):
        self._id = id
        self._pw = pw
        # 인스턴스 속성들은 private으로 처리하여 직접 접근하지 못하도록 하고
        # 이들에 대응되는 property와 setter를 정의하여 캡슐화를 구현

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        raise ValueError('You can\'t change your ID.')

    @property
    def pw(self):
        return self._pw

    @pw.setter
    def pw(self, value):
        if self._pw == value:
            raise ValueError('New password must be different from current password.')
        else:
            self._pw = value
