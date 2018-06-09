# https://docs.python.org/3/library/pickle.html
import pickle
# https://github.com/python/cpython/blob/3.6/Lib/pickle.py
# pickle 모듈은 파이썬 객체를 직렬화/역직렬화하기 위한 binary protocol을 구현하고 있다
# 파이썬 객체를 바이트 스트림으로 변환하는 것을 pickling이라고 하고, 역방향으로 변환하면 unpickling이라고 한다
# Pickling은 보편적으로 serialization, marshalling, flattening이라고도 부른다

some_dictionary = {'key1': 12, 'key2': 4}
# Pickling하기 위한 딕셔너리

pickle.dump(some_dictionary, open('sample.p', 'wb'))
# 바이너리 타입으로 연 파일 객체에 대해 딕셔너리를 pickling하여 저장

res = pickle.load(open('sample.p', 'rb'))
# 바이너리 타입으로 연 파일 객체를 통해 데이터를 unpickling

print(res)
# 딕셔너리가 성공적으로 출력되고
print(type(res))
# 타입 또한 딕셔너리 그대로 들어온다

print(pickle.dumps(some_dictionary))
# bytes 타입으로 pickling된 바이너리 데이터를 반환

print(pickle.loads(pickle.dumps(some_dictionary)))
# pickling된 바이너리 데이터를 파이썬 객체로 변환

# 파이썬에는 marshal이라는 원시적인 직렬화 모듈이 존재하는데, marshal은 일반적으로 파이썬의 .pyc 파일을 지원하기 위해 존재하며 피클은 파이썬 객체를 직렬화하기 위해 선호됨
# 피클은 이미 직렬화된 객체를 다루므로 나중에 동일한 객체에 대한 참조가 다시 직렬화되지 않으며
# marshal로는 불가능한 '사용자 정의 클래스의 인스턴스에 대한 직렬화'도 가능하다
# 또한 marshal의 직렬화 포맷은 파이썬 버전 간에 이식성이 보장되지 않는다
