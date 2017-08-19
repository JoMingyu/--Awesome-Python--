import json
# Json은 아무리 강조해도 지나치지 않을만큼 중요하다
# 파이썬의 json 모듈은 딕셔너리와 문자열 간 변환을 돕는다

# json 모듈에서 중요한 함수는 딱 2개
json_str = '{"key1": 1}'
json_obj = json.loads(json_str)
json_obj['key2'] = 2
print(json_obj)
print(type(json_obj))
# loads : 문자열을 딕셔너리로

print(json.dumps(json_obj))
# dumps : 딕셔너리를 문자열로
