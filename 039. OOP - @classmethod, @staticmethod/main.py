class C:
    @classmethod
    def cls(cls):
        # 클래스 메소드는 첫 인자로 클래스 자신을 나타내는 cls를 받아가기 때문에, 상속 관계 등으로 클래스들이 연관되어 있더라도
        # 항상 올바른 클래스를 인스턴스화시켜줄 수 있음
        # 첫번째 파라미터로 받는 cls를 함수에 넘겨주면 참조 형태가 되기 때문에, 다른 함수에 넘겨줘서 컨트롤 가능하기도 함
        print('Here is class method')
        print(cls)

    @staticmethod
    def static():
        # 호출된 클래스(cls)나 인스턴스(self)에 대해 아무 것도 모르는 메소드
        # 기본적으로 파이썬에선 쓸모가 없으며, 차라리 모듈 레벨 함수를 사용하는 것이 더 좋다는 의견이 많음
        print('Here is static method')

# 1. 둘 다 인스턴스 없이 즉시 호출 가능하다
C.static()
C.cls()

# 2. 객체를 통해서도 접근 가능하다
obj.static()
obj.cls()