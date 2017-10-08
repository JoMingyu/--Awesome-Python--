class C:
    # 데코레이터 파트에서 봤던 __call__이다
    def __init__(self, data):
        self.data = data

    def __call__(self):
        # 이렇게 더블 언더스코어로 둘러싸인 메소드를 매직 메소드라고 부른다
        print(self.data)

obj = C("I'm hungry")
obj()
# 단순히 클래스의 인스턴스를 call하는 것처럼 보이는데, 이게 __call__로 넘어간다
# __call__은 데코레이터를 구현할 때 많이 쓰이는 메소드다
