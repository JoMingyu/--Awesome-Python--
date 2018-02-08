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
