class C:
    @staticmethod
    def static():
        print('Here is static method')

    @classmethod
    def cls(cls):
        print('Here is class method')
        print(cls)

C.static()
C.cls()
# 1. 일단 둘 다 인스턴스 없이 즉시 호출 가능하다

# 2. 먼저 staticmethod는 평소 알고 있던 정적 메소드와 비슷하다
# 클래스를 통해 직접 접근하고, 함께 공유하는 것이다. 그런데 다음을 보자
obj = C()
obj.static()
# 객체를 통해 정적 메소드를 호출할 수가 있다. 이 표현은 Java나 C++에선 warning이다

# 3. 클래스 메소드도 객체를 통해 호출이 된다.
obj.cls()

# 도대체 무슨 차이일까 ㅡㅡ
# 정적 메소드는 호출된 클래스나 인스턴스에 대해 전혀 아무것도 모르는 메소드임
# 따라서 암시적인 첫번째 매개변수(self, cls)가 없음
# 기본적으로 파이썬에선 쓸모가 없다고 봄. 정적 메소드 대신 모듈 함수를 사용하던지 할 듯

# 클래스 메소드는 첫 인자로 cls를 받아가기 때문에, 상속 관계 등으로 클래스들이 연관되어 있더라도
# 항상 올바른 클래스를 인스턴스화시켜줄 수 있음
# 첫번째 파라미터로 받는 cls를 함수에 넘겨주면 참조 형태가 되기 때문에, 다른 함수에 넘겨줘서 컨트롤 가능하기도 함
