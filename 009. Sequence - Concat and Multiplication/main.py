# Sequence는 정수 인덱스를 통한 요소 접근을 지원하는 __getitem__() 메소드와
# 객체의 길이를 반환하는 __len__()이 구현되어 있는 객체를 말한다
# https://docs.python.org/3/glossary.html#term-sequence
# '순서가 보장'되는 유한 개 요소의 열거라고 생각하면 된다
# 대표적인 sequence 객체로는 list와 tuple이 있으며, 이들은 인덱싱, 슬라이싱, 더하기, 곱하기 연산이 가능하다는 특징이 있다

# -- List
l = [1, 2, 3, 4, 5]

print(l + [4, 3, 7])
# [1, 2, 3, 4, 5, 4, 3, 7]

print(l * 2)
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# -- Tuple
t = 1, 2, 3, 4, 5

print(t + (4, 3, 3))
# (1, 2, 3, 4, 5, 4, 3, 3)

print(t * 2)
# (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Dictionary의 경우 Sequence의 필요조건인 __len__()과 __getitem__() 메소드가 정의되어 있지만
# __getitem__()에 정수가 아닌 임의의 불변 키를 사용하기 때문에 Sequence가 아니라 Mapping으로 분류한다
d = {1: 10, 2: 20}
print(d[1])
# index가 아닌 key를 통한 접근

# Tuple의 경우 __getitem__()이 구현되어 있지 않아 Sequence로 분류하지 않음