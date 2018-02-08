# PEP8 스타일을 지키는 것은 정말 중요하다

# Whitespace
# 파이썬에서, 공백(whitespace)은 문법적으로 아주 중요함
# 파이썬 프로그래머들은 특히 공백이 코드 명료성에 미치는 영향에 민감하다
# 1. indent를 위해 tab 대신 space를 사용한다
# 2. indent 레벨 하나 당 4개의 space를 사용한다
# 3. 한 라인에 들어가는 문자는 79개 이하여야 한다
# 4. 길다란 코드를 연결해야 한다면, 새로운 라인(continuation line)에 4개의 space를 추가하여 이어가도록 한다
lst = [i ** 2 + 3 for i in range(100) if i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
       or (i % 2 == 0
           and i % 3 == 1)]
# 5. 파일(모듈)에서 함수와 클래스는 2개의 빈 라인을 두고 구분되어야 한다


def func1(*, arg=0):
    print(arg)


def func2():
    pass

# 6. 클래스에서 메소드들은 1개의 빈 라인을 두고 구분되어야 한다


class C:
    def method1(self):
        pass

    def method2(self):
        pass
# 7. 리스트 인덱싱과 슬라이싱, 함수 호출, 키워드 인수 할당에 공백을 두지 말아야 한다
print(lst[1])
print(lst[3:5])
func1(arg=0)

# Naming
# 1. 함수, 변수, 어트리뷰트(클래스의 필드)는 스네이크 케이스를 사용한다
# 2. protected는 single leading underscore로 표현한다
_protected = 3
# 3. private는 double leading underscore로 표현한다. 인터프리터에 의해 맹글링되기 때문
__private = 5
# 4. 클래스와 예외는 파스칼 케이스(CapitalizedWord)로 작성한다
# 5. 모듈 레벨 상수는 모두 대문자로 표현한다
CONSTANT = 100
# 6. 클래스의 인스턴스 메소드는 첫 파라미터로 self라는 이름을 사용해야 한다
# 7. 클래스 메소드는 첫 파라미터로 cls라는 이름을 사용해야 한다

# Expressions and Statements
# 1. 참에 대한 부정보다 인라인 부정을 사용한다
if not True is True:
    # 참에 대한 부정
    pass
if True is not True:
    # 인라인 부정
    pass
# 2. empty value에 대한 참/부정을 판단하기 위해 length checking을 하지 말자
if len([1, 2, 3]) > 0:
    # length checking
    pass

if [1, 2, 3]:
    # []와 ''는 False, 데이터가 들어가 있을 경우 True임을 이용
    pass
# 3. 한 줄에 if statement와 for, while loop를 표현하려고 하지 말자. 차라리 여러 줄에 나눠 쓰는게 명료하다
# 4. 모든 import statement는 모듈의 최상위에 두도록 하자
# 5. import에선 되도록 상대경로보단 절대경로를 사용하자
# 6. 상대경로를 사용해야 한다면 명시적으로 표현하도록 하자(from . import any)
# 7. 표준 모듈, 서드파티 모듈, 사용자 정의 모듈 순으로 import하며 알파벳 순으로 정렬하자

print('Always follow the PEP8 style guide when writing Python code.')
# https://www.python.org/dev/peps/pep-0008/
