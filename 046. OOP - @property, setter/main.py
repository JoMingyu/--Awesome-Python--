# Python은 필드의 캡슐화에 고전적인 형태의 getter/setter를 사용하지 않고, property 개념을 사용한다
# property는 메소드를 마치 속성에 접근하는 것처럼 보이도록 만들어 주어 getter/setter보다 명료하고 보기 좋다

class PropertyTest:
    def __init__(self, name, color):
        self._name = name
        self._color = color
        # private을 표현하기 위한 문법. underscore 쪽에서 다시 설명한다

    @property
    def name(self):
        # property 함수의 이름은 어떻게 지어도 상관없으나, 사용하려는 속성 이름과 유사하게 지어주는 것이 좋다
        # 단, 속성 이름과 동일하면 에러가 발생하므로 조심해야 한다
        return {'name': self._name}

    @name.setter
    # @[property_function_name].setter
    # 값 할당(=) 연산자를 오버라이딩해 준다
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
# property 메소드의 반환값
