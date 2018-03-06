# https://docs.python.org/3/library/time.html
# time 모듈을 이용해 시간에 관한 조작을 할 수 있다
import time

## 1. 타임스탬프
now = time.time()
print(now, type(now))
# 타입은 float, 소수점 뒤쪽은 초 단위(ns까지 표기)
##

## 2. timestamp와 datetime과의 상호 변환
from datetime import datetime

# (1) timestamp를 datetime으로(time.timestamp -> datetime.datetime)
now_dt = datetime.fromtimestamp(now)
# datetime은 classmethod로 fromtimestamp() 지원
# float 형태의 timestamp를 받아 datetime 객체로 바로 변환

# (2) datetime을 timestamp로(datetime.datetime -> time.struct_time -> time.timestamp)
now_ts = time.mktime(now_dt.timetuple())
# time 모듈에 명시된 함수 중에는 timestamp 변환을 위해 datetime 객체를 지원하는 함수가 없으므로 time.struct_time 객체로 바꿔 줘야 함
# datetime 객체의 timetuple() 메소드는 datetime 객체를 time.struct_time 객체로 바꿔서 리턴
# mktime에서 허용하는 인자의 타입은 오직 time.struct_time이므로 datetime 객체는 struct_time을 거쳐 timestamp로 변환 가능
##

## 3. timestamp와 time.struct_time과의 상호 변환
# (1) timestamp를 struct_time으로(time.timestamp -> time.struct_time)
struct_time = time.gmtime(now)
# 전달된 타임스탬프를 UTC 기준의 time.struct_time 타입으로 변경
struct_time = time.localtime(now)
# 전달된 타임스탬프를 로컬 타임존 기준의 time.struct_time 타입으로 변경
# timestamp를 datetime 객체로 변환하려 한다면, 굳이 필요 없는 과정이며 ms 단위는 사라지므로 주의 필요
# - 'Sun Mar 15 18:49:28:2009' 형태로 반환하는 asctime() 함수가 있음
print(struct_time)
# tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst 필드 존재
# 각각 년도, 월, 일, 시, 분, 초, 요일(int), 1월 1일부터 타임스탬프까지의 누적 날짜, 서머타임(-1, 0, 1)을 나타냄
#

# (2) struct_time을 timestamp로(time.struct_time -> time.timestamp)
print(time.mktime(struct_time))
# 위에서 사용했던 time.struct_time 객체를 타임스탬프로 변경하는 mktime()
# time.struct_time 객체를 사용자가 정의한 형식으로 변경하여 문자열로 반환하는 strftime()
# 사용자가 정의한 형식 문자열을 struct_time 객체로 반환하는 strptime() 함수가 있음
##

## 4. time.time()은 로컬 타임존 기준이며, 따라서 UTC timestamp를 얻으려면
# (1) datetime.utcnow()를 이용(datetime.datetime -> time.struct_time -> time.timestamp)
print(time.mktime(datetime.utcnow().timetuple()))

# (2) time.gmtime()을 이용(time.timestamp -> time.struct_time -> time.timestamp)
print(time.mktime(time.gmtime(time.time())))
##
