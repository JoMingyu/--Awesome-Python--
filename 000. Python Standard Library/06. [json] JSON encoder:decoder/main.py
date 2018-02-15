# https://docs.python.org/3/library/json.html
import json
# 파이썬의 json 모듈은 파이썬 기본 자료형인 list, dictionary와 문자열 간 변환을 돕는다

# json 모듈에서 중요한 함수는 딱 2개
json_str = '{"key1": 1}'
json_obj = json.loads(json_str)
json_obj['key2'] = 2
print(json_obj)
print(type(json_obj))
# loads : 문자열을 파이썬 자료형으로
# JSON 형태의 문자열 내에서, 문자열을 둘러싸는 따옴표는 큰따옴표만 유효하다

print(json.dumps(json_obj))
# dumps : 파이썬 자료형을 문자열로
