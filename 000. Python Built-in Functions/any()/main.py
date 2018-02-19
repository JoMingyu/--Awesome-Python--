"""
   Return True if bool(x) is True for any x in the iterable.

   If the iterable is empty, return False.
"""

# any 함수는 all 함수와 마찬가지로, 인자로 반복가능한(iterable) 객체를 받는다.
# all 함수의 반대개념으로 생각하면 된다.
# 이터레이블 객체의 요소들 중, 하나라도 참이면 True 를 반환한다.

# 맨 마지막 요소 하나가 참이므로 True
print(any([False, False, False, True]))

# 모두 거짓이면 False
print(any([0, 0, 0, 0]))

# any 함수는 all 함수와 다르게 비어있는 이터레이블 객체가 인자로 들어오면 False 를 반환한다.
print(any([]))


# any 함수의 원본
# all 함수의 코드와는 반대로 for 루프를 돌면서 요소 중, 참이 있다면 바로 True 를 반환하고, 아무 요소도 조건문에 걸리지 않으면 False 를 반환한다,
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
