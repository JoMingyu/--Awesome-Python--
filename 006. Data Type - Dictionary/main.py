# key-value 형식의 데이터는 어딜 가든 중요하게 여긴다
# 자바의 hashmap이나 js의 객체나 json 같은거
# 파이썬은 딕셔너리(dictionary)라고 한다
# 키를 가지고 값을 얻어내는 게 사전같아서 그런가보다
# 선언은 당연히 간단하다
dic = {'hello': 3, 'asdf': 4, 123: 123}
# 데이터 타입이 정말 유연하다
# 키는 중복되면 안된다

# 값 얻어내는 건 인덱싱처럼 하면 된다
print(dic['hello'])
print(dic[123])

# key-value 쌍 삭제하는 건 리스트 때 했던 거
del dic[123]

# 추가하는 건
dic['new'] = 1234
print(dic['new'])

# 딕셔너리에 있는 모든 키들을 가져올 필요가 있지 않을까
print(dic.keys())
# 근데 타입이 dict_keys 타입이다
# 리스트로 바꾸려면 그냥 리스트로 캐스팅하면 된다
print(list(dic.keys()))
# value들을 가져올 수도 있다
print(dic.values())
