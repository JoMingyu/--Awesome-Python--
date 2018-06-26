# 새로운 list/tuple을 생성하며, iterable 객체를 인자로 전달하면 해당 객체의 item으로 이루어진 list/tuple 반환
# class list([iterable])
# class tuple([iterable])

print(list())
# []
print(tuple())
# 아무 인자도 전달되지 않으면, 빈 list/tuple이 생성된다

print(list('abc'))
# ['a', 'b', 'c']
print(tuple('abc'))
# ('a', 'b', 'c')

print(list((1, 2, 3)))
# [1, 2, 3]
print(tuple((1, 2, 3)))
# (1, 2, 3)

print(list({1: 2, 2: 3, 5: 4}))
# [1, 2, 5]
print(tuple({1: 2, 2: 3, 5: 4}))
# (1, 2, 5)

print(list([1, 2, 3]))
# [1, 2, 3]
# 전달된 iterable 객체가 이미 list인 경우, iterable[:] 구문을 통해 copy를 만들어 반환한다
print(tuple([1, 2, 3]))
# (1, 2, 3)

# Pure Python으로 구현한 list()

def list_(obj=None):
    if not obj:
        return []
    else:
        if isinstance(obj, list):
            return obj[:]
        else:
            if not hasattr(obj, '__iter__'):
                raise TypeError('{} object is not iterable'.format(str(type(obj))[6:-1]))
            else:
                return [item for item in obj]

# Pure Python으로 구현한 tuple()

def tuple_(obj=None):
    if not obj:
        return []
    else:
        if not hasattr(obj, '__iter__'):
            raise TypeError('{} object is not iterable'.format(str(type(obj))[6:-1]))
        else:
            return tuple(item for item in obj)