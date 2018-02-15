# Python 3부턴 Dictionary Comprehension, Set Comprehension을 추가로 지원한다
_list = [i * 2 for i in range(20)]
print(_list)

_set = {i * i for i in range(10)}
print(_set)

_sample = {'key1': 1, 'key2': 2, 'key3': 3}
_dict = {k: v * 2 for k, v in _sample.items()}
print(_dict)
