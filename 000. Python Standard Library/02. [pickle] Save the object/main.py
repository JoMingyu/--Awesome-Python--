# https://docs.python.org/3/library/pickle.html
# pickle 모듈은 객체를 파일에 저장할 수 있음
# 생각보다 훨씬 엄청난 메리트
import pickle

some_dictionary = {'key1': 12, 'key2': 4}
# 저장하기 위한 딕셔너리를 만들어 보자

pickle.dump(some_dictionary, open('sample.p', 'wb'))
# 바이너리 타입으로 연 파일 객체에 대해 딕셔너리를 저장

res = pickle.load(open('sample.p', 'rb'))
# 바이너리 타입으로 연 파일 객체를 통해 데이터를 불러옴

print(res)
# 딕셔너리가 성공적으로 출력되고
print(type(res))
# 타입마저 딕셔너리 그대로 들어온다
