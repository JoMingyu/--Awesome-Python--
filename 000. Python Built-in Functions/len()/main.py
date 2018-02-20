""" Return the number of items in a container. """

# len 함수는 인수로 들어온 객체의 길이(요소 수)를 반환한다.
# 인자로는 시퀀스 자료형이나 컬렉션(dictionary, set 등)을 받는다
# 시퀀스 자료형은 인덱싱이 가능한 string. bytes, list, tuple, range 등을 말한다.

# 아래의 list, tuple, range 의 요소의 개수인 3, 5, 4 를 각각 반환
print(len([1, 2, 3]))
print(len((10, 9, 8, 7, 6)))
print(len(range(1, 5)))

# 아래의 string 과 bytes 의 길이인 13, 15를 각각 반환(공백 포함)
print(len("Life is short"))
print(len(b"you need python"))

# 아래의 dictionary 와 set 의 길이인 2, 5를 각각 반환
print(len({'key1': '1', 'key2': 2}))
print(len({1, 2, 3, 4, 5}))


# len() 은 내부적으로 인자로 들어온 객체의 매직 메서드 __len__() 을 호출하므로
# Pure python code 로 len 함수를 표현한다면
def len(s):
    if hasattr(s, '__len__'):
        # 객체에 __len__ 이 있다면 호출
        return s.__len__()
    else:
        # __len__ 이 없으면 typeerror
        raise TypeError

