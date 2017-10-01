import re
# re는 정규 표현식(Regular Expression)을 위한 모듈

# 1. re에 갖다대고 찾을 수 있다
print(re.findall('\\d+', '123a1234'))

# 2. 정규 표현식을 컴파일해서 패턴 객체를 얻을 수 있다
regex = re.compile('\\w+')
# 그럼 패턴에 대해 문자열을 찾을 수 있다. findall() 함수는 정규식과 맞는 문자열들을 리스트로 반환한다
groups = regex.findall('123!1231.asd')

# match와 search가 있다

# (1) match는 정규식과 매치되는지 판단한다(문자열의 처음부터 봄)
match = regex.match('!123')
# 정규식에 맞지 않을 땐 None이 리턴된다

# 정규식에 맞으면 match 객체가 리턴된다
match = regex.match('123')
# match 객체는 group(), start(), end(), span() 함수를 가지고 있다.
# 각각 문자열 리턴, 시작 위치 리턴, 끝 위치 리턴, 시작 위치와 끝 위치에 해당되는 튜플 리턴이다
print(match.group(), match.start(), match.end(), match.span())
# match 함수는 정규식에 맞는지를 판단하기 위해서 사용하곤 한다(None이면 안맞고, None이 아니면 맞다고 판단)

# (2) search는 정규식 매치를 문자열 전체에서 본다
search = regex.search('!123')
# match에선 None이 리턴됐던 문자열이지만 search는 문자열 전체를 보므로 match 객체가 잘 리턴된다
print(search.group())
