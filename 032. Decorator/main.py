# 벌써 데코레이터를 해도 되나 모르겠다. 자바의 어노테이션과 비슷하지만 많이 다르다
# 기본적으로 본체를 꾸며주는 역할을 한다

# 일단 기본적인 데코레이터를 선언해보자


class Deco:
    def __init__(self, f):
        # 데코레이터가 함수를 꾸며주고 있다는 것을 뜻함
        print('Decorator initialized')
        self.function = f
        # self로 해당 요소를 가지고있지 않으면 제대로 동작하지 않는다
        # - 함수가 실행되지 않는 등

    def __call__(self):
        print('Called')
        self.function()


@Deco
def func():
    print('Hello')

func()
# 아직은 데코레이터를 제대로 모르고 있으니 이만큼만 하고 일단 넘어가도록 하자
