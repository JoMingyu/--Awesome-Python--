# 함수의 키워드 인자에 할당한 기본값은 함수가 바인딩될 때에 한 번만 평가된다
import time

def get_gmt_time(t=time.time()):
    return time.gmtime(t)

print(get_gmt_time())
time.sleep(3)
print(get_gmt_time())
# 3초가 지난 이후, time.struct_time 객체의 time_sec이 3초가 늘어나 있어야 하나,
# get_gmt_time 함수를 최초 실행했을 때 인자 t의 기본값이 평가되고, 해당 값으로 고정되어 두 print의 출력값이 동일해진다
# 따라서 위와 같은 문제를 해결하기 위해선, 기본값을 None으로 두고 docstring과 함께 함수를 작성하는 것이 좋다

def get_gmt_time(t=None):
    """
    Args:
        t (float) : GMT struct_time으로 변환할 timestamp, 별도로 전달되지 않은 경우 time.time()을 사용합니다.
    """
    if t is None:
        t = time.time()

    return time.gmtime(t)

print(get_gmt_time())
time.sleep(3)
print(get_gmt_time())