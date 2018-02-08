# 크롤링 준비 3번째 - re
# 파이썬 내장 패키지
import re
# 정규표현식에 관한 일들을 돕는 모듈

pattern = re.compile('[a-z]+')
# 패턴 컴파일
print(type(pattern))
# <class '_sre.SRE_Pattern'>

# 패턴 객체에서 정규 표현식 검사를 할 수도 있고, re의 함수에 접근하여 그 즉시 패턴을 입력할 수도 있음
# findall은 정규 표현식에 맞는 모든 문자열을 리스트로 리턴
print(pattern.findall('asdf123asd'))
print(re.findall('[a-z]+', 'asdf123asd'))
# 아래의 경우 함수 내에서 pattern을 컴파일한 이후 find를 돌리기 때문에 속도 면에서 손해를 볼 가능성이 있음

print(pattern.sub('replaced', 'asdf123asd'))
# 문자열 replace를 정규표현식으로 수행. repl, str 순서
# 해당 패턴에 맞는 문자열을 repl로 교체 후 반환

print(pattern.search('12asd45qw'))
# 주어진 string 전체를 pattern으로 검색하여 일치하는 문자열을 찾아 match object로 반환
# 문자열 전체에 대해 검색. 아래의 match 메소드와 대비됨
print(pattern.match('12asd45qw'))
# match object가 반환되지 않음. 문자열의 처음부터 검색하기 때문
