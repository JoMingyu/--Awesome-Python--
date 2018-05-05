# Python은 필드의 캡슐화에 고전적인 형태의 getter/setter를 사용하지 않고, property 개념을 사용한다
# single leading underscored 네이밍을 통해 필드를 암시적으로 private으로 만든 뒤, property와 setter 메소드를 정의한다
class PropertyTest:
    def __init__(self, name, color):
        self._name = name
        self._color = color

    @property
    def name(self):
        # property 함수의 이름은 어떻게 지어도 상관없으나,
        # 객체에선 필드에 접근하는 것처럼 해당 property에 접근하므로 캡슐화한 변수 이름에서 언더스코어를 제거한 이름을 사용하는 것이 좋다
        return {'name': self._name}

    @name.setter
    # @[property_function_name].setter
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
# 객체의 필드에 직접 접근하는 것처럼 보이지만, 실제로는 setter 메소드에 접근

print(prop_test.name, prop_test.color)
# 객체의 필드가 아닌 property 메소드의 반환값