"""
Create a new dictionary. The dict object is the dictionary class.
See dict and Mapping Types — dict for documentation about this class.

For other containers see the built-in list, set, and tuple classes,
as well as the collections module.
"""

# Iterable 객체를 받아 새로운 딕셔너리 객체를 생성한다
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)

print(dict())
# {}
# 아무 인자도 전달되지 않으면, 빈 딕셔너리가 생성된다(class dict(**kwarg))

print(dict([(1, 3), (2, 5), (3, 'hi'), (1, 'hello')]))
# {1: 'hello', 2: 5, 3: 'hi'}
# 위치 인자가 전달되고,
# (1) class dict(mapping, **kwarg) : 해당 인자가 mapping 객체라면 해당 객체와 동일한 key-value pair를 가진 딕셔너리가 생성,
# (2) class dict(iterable, **kwarg) : 각 item이 정확히 두 개의 객체씩을 가지는 iterable 객체인 경우(위의 경우)
# iterable 객체에 들어 있는 item의 첫 원소를 key로, 두 번째 원소를 value로 하는 딕셔너리가 생성된다
# key가 겹치는 상황이 생기면, 가장 마지막 value가 할당된다

print(dict(a=3, b=4))
# {'a': 3, 'b': 4}
# 키워드 인자가 전달되면, 위치 인자를 통해 생성된 dictionary에 해당 키워드 인자 매핑이 추가됨
# key가 겹치는 상황이 생기면, 키워드 인자의 value가 위치 인자의 value를 대체한다