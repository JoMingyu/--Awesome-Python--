# https://docs.python.org/3/library/datetime.html
# 시간을 다루는 datetime 모듈
import datetime

# 먼저 datetime은 두 개의 상수를 지원한다
print(datetime.MINYEAR)
print(datetime.MAXYEAR)

# date, time, datetime, timedelta, tzinfo, timezone 클래스가 있다

# - date
date = datetime.date(2017, 8, 7)
# 숫자로 년, 월, 일을 받아서 date 객체를 생성
# default로 지정되어 있는 값이 없으므로 인자가 모두 들어가야 한다

print(date.weekday())
# 요일. 월요일이 0, 일요일이 6
# isoweekday, isocalendar, isoformat 등을 지원한다

today = datetime.date.today()
# 오늘을 기준으로 객체를 생성할 경우
print(today.day)

# 아래의 class attribute들을 지원한다
print(datetime.date.min)
# date(MINYEAR, 1, 1)
print(datetime.date.max)
# date(MAXYEAR, 12, 31)
print(datetime.date.resolution)

# 아래의 instance attribute들을 지원한다
print(date.year, date.month, date.day)

# - time
time = datetime.time(10, 15, 14)
# time 객체 생성
# hour, minute, second, microsecond를 받지만 모두 0으로 디폴트 값이 지정되어 있음

# 현재 시간을 기준으로 객체 생성은 불가능. datetime 클래스의 도움을 받아야 한다
print(datetime.datetime.today().time())

# 아래의 class attribute들을 지원한다
print(datetime.time.min)
# time(0, 0, 0, 0)
print(datetime.time.max)
# time(23, 59, 59, 999999)
print(datetime.time.resolution)

# 아래의 instance attribute들을 지원한다
print(time.hour, time.minute, time.second, time.microsecond, time.tzinfo, time.fold)

# - datetime
dt = datetime.datetime(2017, 8, 7)
# datetime 객체 생성
# 생성자 매개변수는 date와 time 클래스를 합쳤다고 생각하면 된다

now = datetime.datetime.today()
# 현재를 기준으로 객체를 생성할 경우
# datetime.datetime.now()도 가능하지만, now(tzinfo=None)는 today()와 같다
# 로컬 타임존을 기준으로 현재를 판단하므로, UTC 기준으로 가져오려면 datetime.datetime.utcnow()를 사용하면 된다
now = datetime.datetime.utcnow()

print(now.date())
# 년, 월, 일만 가져오기

print(now.time())
# 시간만 가져오기

# 아래의 class attribute들을 지원한다
print(datetime.datetime.min)
# datetime(MINYEAR, 1, 1, tzinfo=None)
print(datetime.datetime.max)
# datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999, tzinfo=None)
print(datetime.datetime.resolution)

# 아래의 instance attribute들을 지원한다
print(now.year, now.month, now.day)

# - 문자열과의 상호 변환

# datetime/date/time 객체의 strftime() 메소드로 time -> str
# datetime.datetime.strptime() 함수로 str -> time 변환할 수 있다

# (1) datetime to str - strftime()
print(now.strftime('%Y-%m-%d %H'))
# datetime 모듈 하위 객체들은 __str__ 연산자를 오버로딩하고 있으며, 내부는 %Y-%m-%d %H:%M:%S.%f 포맷으로 변환하여 리턴한다
print(str(now))

# (2) str to datetime - strptime()
print(datetime.datetime.strptime('2017-01-03', '%Y-%m-%d'))
# 기타 포매팅은 여기서 확인하자 : https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# - 날짜 객체 간의 계산

# datetime 모듈의 date, time, datetime은 연산자 오버로딩을 지원하기 때문에 계산하기 굉장히 편하다
# 날짜 객체의 사칙연산에서는 timedelta(시차)의 개념이 등장한다
from datetime import date, time, datetime, timedelta

d1 = date(2017, 11, 13)
d2 = date(2017, 9, 8)

print(type(d1 - d2))
# date 객체 간 계산 시 timedelta 객체 리턴

print(d1 - d2)
# timedelta 객체는 property로 days, seconds, microsecnds가 있음

print((d1 - d2).days)
# 두 날짜 간 일수 차이

print()

dt1 = datetime(2017, 11, 13)
dt2 = datetime(2017, 9, 8)

print(type(dt1 - dt2))
print(dt1 - dt2)
print((dt1 - dt2).seconds)
# 예상과 달리 seconds(두 날짜 간 초 차이)는 0이 리턴됨
# seconds는 date 부분을 무시하고 time 부분에서의 시차를 다루기 때문에
# hour, minute, second, microsecond가 0으로 세팅된 두 객체 간의 second 차이는 0
# 참고로 time 클래스는 사칙연산에 대한 연산자 오버로딩이 지원되지 않음

if dt2 < dt1:
    # le, ge, lt, gt 메소드가 오버로딩되어 있음
    print('dt1 is over than dt2')
