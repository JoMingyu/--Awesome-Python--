# https://docs.python.org/3/library/re.html
import re
# 정규표현식에 관한 일들을 돕는 모듈

pattern = re.compile('[a-z]+')
# 정규 표현식 패턴을 regular expression 객체로 컴파일
print(type(pattern))
# <class '_sre.SRE_Pattern'>

# 패턴 객체에서 정규 표현식 검사를 할 수 있고
print(pattern.findall('asdf123asd'))
# findall은 정규 표현식에 맞는 모든 문자열을 리스트로 리턴

print(pattern.sub('replaced', 'asdf123'))
# 문자열 replace를 정규표현식으로 수행. regex.sub(repl, string)
# 문자열에서 해당 패턴에 맞는 부분을 repl로 교체 후 반환

print(pattern.search('1asd123'))
# 주어진 string 전체를 pattern으로 검색하여 일치하는 문자열을 찾아 match object로 반환
# 패턴에 맞는 문자열이 없으면 None 반환
# 문자열 전체에 대해 검색. 아래의 match 메소드와 대비됨

print(pattern.match('1asd123'))
# 주어진 string에 대해 첫 인덱스를 기준으로 일치하는 문자열을 찾아 match object로 반환
# 문자열의 첫 인덱스부터 [a-z]+ 패턴으로 검사하므로 None이 반환됨
# match의 시작 인덱스를 설정해줄 수 있음

print(pattern.match('1asd123', 2))
# 2번 인덱스('s') 부터 검색하므로 'sd'를 가진 match object가 반환됨

# match object는 group() 메소드를 이용해서 검출된 문자열을 가져올 수 있음
print(pattern.match('1asd123', 2).group())
# https://docs.python.org/3/library/re.html#match-objects

print(pattern.fullmatch('as1df'))
# fullmatch는 문자열 전체가 regex에 맞는지를 검사

print(pattern.fullmatch('as1df', 3))
# 3번 인덱스('d') 부터 fullmatch를 판단하므로 'df'를 가진 match object가 반환됨

# re의 함수에 접근하여 그 즉시 패턴 매칭도 가능하다
print(re.findall('[a-z]+', 'asdf123asd'))
# 이 경우 함수 내에서 pattern을 컴파일한 이후 find를 돌리기 때문에 속도 면에서 손해를 볼 가능성이 있음
