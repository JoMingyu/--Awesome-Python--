"""
Return a new set object, optionally with elements taken from iterable. set is a built-in class.
See set and Set Types — set, frozenset for documentation about this class.
"""

# 새로운 set 객체를 생성하며, iterable 객체를 인자로 전달하면 해당 객체의 item으로 이루어진 set 반환
# class set([iterable])

print(set())
# set()
# 인자 미전달 시 빈 set 반환

print(set('abcdc'))
# {'c', 'b', 'd', 'a'}
# 순서가 보장되지 않으며, 중복을 허용하지 않으므로

print(list(set([1, 2, 2, 3, 4, 4, 4, 5])))
# [1, 2, 3, 4, 5]
# 타 iterable 객체의 중복 제거 용도로도 사용 가능