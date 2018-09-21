# NotImplementedError라는 빌트인 에러 클래스를 이용해, 추상 메소드를 표현할 수 있다


class Base:
    def run(self):
        raise NotImplementedError()


class Implement(Base):
    def run(self):
        print('running!')


class Ignore(Base):
    pass
    # NotImplementedError는 추상 메소드를 표현하는 거의 유일한 방법이지만, 단지 추상 메소드임을 '표현'하기 위함이라,
    # 강제성을 가지고 있지 않으므로 run 메소드를 정의하지 않아도 상관 없다
    # PyCharm에선 이 클래스가 warning으로 표시되며, 에러가 발생하지는 않는다
    # Python의 '개발자를 믿고 자유도를 높이는' 문화 중 하나

o = Implement()
o2 = Ignore()

print(o.run())
