# Sequence는 정수 인덱스를 통한 요소 접근을 지원하는 __getitem__() 메소드와
# 객체의 길이를 반환하는 __len__()이 구현되어 있는 객체를 말한다(순서가 보장되는 유한 개 요소의 열거)
# List, Tuple, String이 대표적인 Sequence 객체

l = [1, 2, 3, 4, 5]
print(l[0])
print(l.__getitem__(0))

print(len(l))
print(l.__len__())

t = 1, 2, 3, 4, 5
print(t.__getitem__(0))
print(t.__len__())

s = 'PlanB'
print(s.__getitem__(0))
print(s.__len__())

# Dictionary의 경우 Sequence의 필요조건인 __len__()과 __getitem__() 메소드가 정의되어 있지만
# __getitem__()에 정수가 아닌 임의의 불변 키를 사용하기 때문에 Sequence가 아니라 Mapping으로 분류한다
# Tuple의 경우 __getitem__()이 구현되어 있지 않아 Sequence로 분류하지 않음
d = {1: 10, 2: 20}
print(d.__getitem__(1))
# index가 아닌 key를 통한 접근
print(d.__len__())