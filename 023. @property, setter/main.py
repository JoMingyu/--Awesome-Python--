# Java에서는 캡슐화 구현을 위해 getter/setter를 구현하지만, Python의 경우 property와 setter를 사용한다
class PropertyTest:
    def __init__(self, name, color):
        self._name = name
        self._color = color
        # 언더스코어 적용으로 변수 자체는 protected 처리

    # 변수명과 같은 이름의 함수로 property와 setter 함수 구현
    @property
    def name(self):
        return {'name': self._name}

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def color(self):
        return {'color': self._color}

    @color.setter
    def color(self, color):
        self._color = color


prop_test = PropertyTest('JoMingyu', 'Black')

prop_test.name = 'MingyuJo'

print(prop_test.name, prop_test.color)
