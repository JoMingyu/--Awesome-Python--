# https://docs.python.org/3/library/datetime.html
# 시간을 다루는 datetime 모듈
# datetime, date, time 클래스가 있다
import datetime

date = datetime.date(2017, 8, 7)
# 숫자로 년, 월, 일을 받아서 date 객체를 생성
# default로 지정되어 있는 값이 없으므로 인자가 모두 들어가야 한다
print(date.year, date.month, date.day, date.weekday())
# weekday는 요일. 월요일이 0, 일요일이 6

today = datetime.date.today()
# 오늘을 기준으로 객체를 생성할 경우
print(today.day)

time = datetime.time(10, 15, 14)
# time 객체 생성

# hour, minute, second, microsecond를 받지만 모두 0으로 디폴트 값이 지정되어 있음
print(time.hour, time.minute, time.second)
# 현재 시간을 기준으로 객체 생성은 불가능. datetime 클래스의 도움을 받아야 한다
print(datetime.datetime.now().time())

dt = datetime.datetime(2017, 8, 7)
# datetime 객체 생성
# 생성자 매개변수는 date와 time 클래스를 합쳤다고 생각하면 된다

now = datetime.datetime.now()
# 현재를 기준으로 객체를 생성할 경우
# datetime.datetime.today()도 가능
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second, now.microsecond)

print(now.date())
# 년, 월, 일만 가져오기

print(now.time())
# 시간만 가져오기
