class C:
    # 클래스에는 재미난 메소드들이 많다
    # 오늘 알아볼 건 __call__
    def __init__(self, data):
        self.data = data

    def __call__(self):
        # 이렇게 더블 언더스코어로 둘러싸인 메소드를 매직 메소드라고 부른다. 나중에 한번 더 공부할거다
        print(self.data)

obj = C("I'm hungry")
obj()
# 단순히 클래스의 인스턴스를 call하는 것처럼 보이는데, 이게 __call__로 넘어간다
