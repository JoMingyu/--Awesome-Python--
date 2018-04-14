# 타 언어에서는 문자를 char로, 문자열을 string으로 따로 관리하는데 비해
# Python에는 문자, 문자열, blank('') 모두 string으로 취급

# -- 문자열 객체 선언
s = 'PlanB'
s = "PlanB"
# 따옴표의 종류에 제한을 두지 않으며, 특별한 상황이 아니라면 작은따옴표 사용

s = '''PlanB's Awesome Python'''
s = """PlanB's Awesome Python"""
# 따옴표 3개를 연속적으로 이어붙여 표현할 수도 있음
# 1. 문자열 안에 작은따옴표나 큰따옴표를 포함시키기 위해서
# 2. 여러 줄에 문자열을 표현하기 위해서
# 큰따옴표 3개를 이어붙인 형태는 docstring이라는 특별한 형태의 주석을 표현하기 위해 사용한다

# -- 문자열 포매팅
# 문자열 안에 특정 값을 삽입하는 것을 말하며, 특정 값은 대체적으로 변수
# 1. 포맷 코드 사용
age = 19
nickname = 'PlanB'
print('My nickname is %s, age is %d' % (nickname, age))

# 2. 문자열 객체의 .format() 메소드 사용
print('My nickname is {0}, age is {1}'.format(nickname, age))
# {0}, {1}과 같은 표현을 보편적으로 placeholder라고 부름

# 3. 인덱스가 제거된 placeholder 사용
print('My nickname is {}, age is {}'.format(nickname, age))
# 순차적으로 전달할 경우 인덱스를 제거해도 되며, 해당 방법을 많이 사용

# 4. fstring
print(f'My nickname is {nickname}, age is {age}')
# Python 3.6부터 지원하며, 아직 자주 사용되진 않음