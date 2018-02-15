# https://docs.python.org/3/library/time.html
# time 모듈을 이용해 시간에 관한 조작을 할 수 있다
import time

now = time.time()
# 1. 타임스탬프
print(now, type(now))
# 타입은 float, 소수점 뒤쪽은 초 단위(ns까지 표기)

# 2. timestamp와 datetime과의 상호 변환
from datetime import datetime

# timestamp -> datetime
now_dt = datetime.fromtimestamp(now)
# datetime은 classmethod로 fromtimestamp() 지원
# float 형태의 timestamp를 받아 datetime 객체로 변환

# datetime -> timestamp
now_ts = time.mktime(now_dt.timetuple())
# time 모듈에 명시된 함수 중에는 timestamp 변환에 datetime 객체를 지원하는 함수가 없으므로 time.struct_time 객체로 바꿔 줘야 함
# datetime 객체의 timetuple() 메소드는 datetime 객체를 time.struct_time 객체로 바꿔서 리턴
# mktime의 매개변수는 time.struct_time 타입이므로 datetime 객체를 timestamp로 변환 가능

# 3. timestamp와 time.struct_time과의 상호 변환
# timestamp -> time.struct_time
struct_time = time.gmtime(now)
# 전달된 타임스탬프를 UTC 기준의 time.struct_time 타입으로 변경
# timestamp에서 ms 단위는 사라지므로 주의 필요
# 지방표준시 기준의 time.struct_time 객체로 변경하는 localtime() 함수
# 'Sun Mar 15 18:49:28:2009' 형태로 반환하는 asctime() 함수가 있음
print(struct_time)
# tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst 필드 존재
# 각각 년도, 월, 일, 시, 분, 초, 요일(int), 1월 1일부터 타임스탬프까지의 누적 날짜, 서머타임(-1, 0, 1)을 나타냄

# struct_time -> timestamp
print(time.mktime(struct_time))
# 위에서 사용했던 time.struct_time 객체를 타임스탬프로 변경하는 mktime()
# time.struct_time 객체를 사용자가 정의한 형식으로 변경하여 문자열로 반환하는 strftime()
# 사용자가 정의한 형식 문자열을 struct_time 객체로 반환하는 strptime() 함수가 있음

# 인자가 전달되지 않은 경우 time.time()의 결과값을 이용하여 현재 시간을 기준으로 변환
