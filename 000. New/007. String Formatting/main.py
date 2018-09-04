# 컴퓨터 프로그래밍에서 string interpolation은
# placeholder가 포함된 문자열 리터럴을 평가하여, placeholder를 특정한 값으로 치환한 결과를 반환하는 프로세스
# Python에서는 string formatting이라고도 이야기한다
# https://www.python.org/dev/peps/pep-3101

nickname = 'planb'
age = 19

# 1. 포맷 코드 사용
print('My nickname is %s, age is %d' % (nickname, age))
# <string literal> % (values)
# C 계열 언어의 printf 역할

# 2. placeholder 표현식과 문자열 객체의 .format() 메소드 사용
print('My nickname is {0}, age is {1}'.format(nickname, age))
# 인자로 전달된 nickname과 age가 각각 {0}, {1}에 치환됨
print('{0} {0} {1}'.format(nickname, age))
# 'planb planb 19'
# 동일한 치환 표현식을 가진 두 개 이상의 placeholder를 함께 사용해, 동일한 값을 여러 번 치환할 수 있다
print('{1} {0}'.format(nickname, age))
# '19 planb'
# 숫자는 format 메소드의 인자로 전달되는 값들 중 어떤 걸 치환할지를 표현하는 것 뿐이라, 순서를 지키지 않아도 됨

# 3. 인덱스가 제거된 placeholder 사용
print('My nickname is {}, age is {}'.format(nickname, age))
# 인자로 전달된 값들을 순차적으로 치환할 경우 인덱스를 제거해도 되며, 해당 방법을 많이 사용

# 4. named placeholder
print('My nickname is {nickname}, age is {age}'.format(nickname=nickname, age=age))
# 이름이 설정된 placeholder와, 각각의 placeholder를 키워드 인자로서 값을 전달
# 동일한 값을 여러 placeholder에 적용하거나, 명시적인 포매팅을 표현하고 싶은 경우에 유용하게 쓰임

# 5. fstring
print(f'My nickname is {nickname}, age is {age}')
# Python 3.6부터 지원하며, JavaScript의 template literal과 비슷한 형태
# 미리 선언해 두고 나중에 포매팅하는 경우가 아니라,
# 문자열 리터럴에 외부의 값을 주입해야 하는 경우 유용하고 다른 포매팅 방식보다 빠르기도 함
