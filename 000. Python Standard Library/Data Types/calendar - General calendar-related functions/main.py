# https://docs.python.org/3/library/calendar.html
# 유닉스의 cal 프로그램과 비슷하게 생긴 달력을 출력할 수 있으며 달력과 관련된 유용한 함수들을 추가로 제공함
import calendar

# 기본적으로 파이썬의 calendar 객체들에서는 월요일이 주 중 첫 번째 날로 표시되며 일요일이 마지막 요일로 표시됨
# 일요일을 첫 번째 날로 설정하자
calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.calendar(2017))
# calendar(year)를 사용해 그 해의 전체 달력을 볼 수 있음

print(calendar.prmonth(2018, 3))
# 해당 year와 month에 해당되는 달력을 볼 수 있음

print(calendar.monthrange(2018, 3))
# 해당 year와 month의 첫 날의 요일과 일의 수를 반환

print(calendar.weekday(2001, 2, 5))
# 해당 year, month, day의 요일을 반환
# 월요일이 0
