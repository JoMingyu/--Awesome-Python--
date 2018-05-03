# https://github.com/sdispater/pendulum
# pip install pendulum
import pendulum
# https://pendulum.eustace.io/
# 표준 datetime 클래스의 drop-in replacement이며 datetime과 결과물은 동일하지만 많은 개선 사항이 있음
# 문서화가 정말 잘 되어 있다

now = pendulum.now('Asia/Seoul')
print(now)
# 2018-04-29T19:34:19.061936+09:00

print(pendulum.now())
# 2018-04-29T19:34:19.061936+09:00
# Timezone 없이 호출하면 local timezone으로 설정

print(pendulum.timezones)
# ('Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', ..., 'WET', 'Zulu')

print(now.in_timezone('America/Toronto'))
# timezone 변경
# 2018-04-29T06:34:19.061936-04:00

print(now.add(days=3))
# 시간 shifting

print(now.tomorrow())
# 2018-04-30T00:00:00+09:00

print(now.yesterday())
# 2018-04-28T00:00:00+09:00

dt = pendulum.datetime(2018, 1, 1, tz='Asia/Seoul')
# datetime.datetime과 동일한 역할이며 인스턴스도 동일
import datetime
print(isinstance(dt, datetime))

# datetime을 대체하기 정말 좋은 라이브러리이고, 문서화도 굉장히 잘 되어 있으므로
# documentation[https://pendulum.eustace.io/docs/]에서 구체적인 설명을 볼 수 있다
