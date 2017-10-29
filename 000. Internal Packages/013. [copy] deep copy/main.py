# copy 모듈을 알아보자. 대부분 deep copy를 손쉽게 구현하기 위해서 사용한다
import copy

_list = [1, 2, 3, [1, 2]]
copied_list = copy.copy(_list)
# Shallow copy
copied_list[3][0] = 999
print(_list, copied_list)

deep_copied_list = copy.deepcopy(_list)
# Deep copy
deep_copied_list[3][0] = -100
print(_list, deep_copied_list)
