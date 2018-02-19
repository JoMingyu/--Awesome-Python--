"""
Return True if bool(x) is True for all values x in the iterable.

If the iterable is empty, return True.
"""

# all 함수는 인자로 반복가능한(iterable) 객체를 받는다
# 이터레이블 객체의 모든 요소가 참이면 True 를 반환하고, 거짓이 하나라도 있으면 False 를 반환한다

# 모두 True(참) 이므로 True
print(all([True, True, True]))

# 요소 중 0(거짓) 이 있으므로 False
print(all([1, 2, 3, 0, 4]))

# 비어있는 이터레이블 객체의 경우에도 True 를 반환한다
print(all([]))


# all 함수 원본
# for 루프를 돌면서 없는 요소가 하나라도 있는지(거짓인지) 조건 검사를 한다
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
