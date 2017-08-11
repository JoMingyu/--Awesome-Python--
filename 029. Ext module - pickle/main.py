# pickle 모듈은 파이썬에서 만들어지는 모든 것을 담을 수 있다고 함
# 생각보다 훨씬 엄청난 메리트
import pickle

some_dictionary = {'key1': 12, 'key2': 4}
# 저장하기 위한 딕셔너리를 만들어 보자

pickle.dump(some_dictionary, open('sample.p', 'wb'))
# wb 타입으로 연 파일 객체에 대해 딕셔너리를 저장했다

res = pickle.load(open('sample.p', 'rb'))
# rb 타입으로 연 파일 객체를 통해 불러왔다

print(res)
# 딕셔너리가 성공적으로 출력되고
print(type(res))
# 타입마저 딕셔너리 그대로 들어온다
# 파일에 쓰는 건 그냥 문자열 자체지만

# 객체 자체를 저장할 수 있다는 게 정말 좋은 메리트다
