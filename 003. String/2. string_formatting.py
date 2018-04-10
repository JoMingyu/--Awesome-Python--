# 문자열 포매팅은 문자열 안에 특정 값을 삽입하는 것을 말함
# - 보편적인(old-style) 문자열 포매팅 방식, 포맷 코드를 사용
format1 = 'My %s is %s!!'
print(format1 % ('Name', 'PlanB'))

# - str 객체의 format 메소드를 이용하는 방식
# placeholder를 포함한 문자열로 포맷을 만들고, format 메소드의 인자로 값들을 넘겨주면 된다
format2 = 'This is {0} formatting{1}'
print(format2.format('awesome', '!'))
# {0} 자리에 'awesome'이, {1} 자리에 '!'가 들어감
# 타입 안정성이 높고, 정렬이나 공백 채우기 등의 고급 포매팅이 가능해서 이걸 많이 쓴다
# https://pyformat.info/ 에 따르면 placeholder에 인덱스를 표기하는 위의 방식 또한 old-style로 분류한다

# 포매팅 시 특별한 일을 수행하지 않는다면 placeholder의 인덱스는 생략 가능하다. 파이썬에서 사용하는 가장 보편적인 포매팅 방식
format3 = '{} {}'
print(format3.format(1, 2))

# 파이썬 3.6의 fstring
data = 'formatting'
print(f"Python 3.6's {data}")
