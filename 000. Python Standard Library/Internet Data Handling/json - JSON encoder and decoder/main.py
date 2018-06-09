# https://docs.python.org/3/library/json.html
import json
# https://github.com/python/cpython/tree/3.6/Lib/json
# JSON은 Javascript 객체의 literal syntax에 영향을 받아 RFC 7159와 ECMA-404에 의해 지정된 경량의 data interchange format이다
# 파이썬의 json 모듈은 파이썬 기본 자료형인 list, dictionary와 JSON 문자열 간 변환을 돕는다

# json 모듈에서 중요한 함수는 딱 2개
json_str = '{"key1": 1}'
json_obj = json.loads(json_str)
json_obj['key2'] = 2

print(json_obj)
print(type(json_obj))
# loads : 문자열을 파이썬 자료형으로
# JSON 형태의 문자열 내에서, 문자열을 둘러싸는 따옴표는 큰따옴표만 유효하다(RFC 7159 - Page 7. Strings)

print(json.dumps(json_obj, sort_keys=True, indent=4))
# dumps : 파이썬 자료형을 문자열로
# sort_keys와 indent처럼 Prettify를 위한 인자를 몇가지 제공한다

# json.JSONEncoder와 json.JSONDecoder 클래스를 상속받아 커스텀 encoder/decoder도 구현할 수 있다
