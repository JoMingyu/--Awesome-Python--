# List와 Tuple의 관계처럼, Frozenset은 선언 후 별도의 add/remove가 불가능한 set으로, read-only set이라 생각할 수 있다
# (공식 문서 인용) - The frozenset type is immutable and hashable — its contents cannot be altered after it is created;

fs = frozenset()
# frozenset()
# 별도의 리터럴 표현식은 없고, 빌트인 함수를 통해 선언 가능
# class frozenset([iterable])

fs = frozenset([
    'a',
    'b',
    'c',
    123,
    'PlanB',
    'PlanB'
])

print(fs)
# frozenset({'b', 'c', 'a', 'PlanB', 123})
# update, intersection_update, add, remove 등 alteration에 해당하는 작업을 제외한 모든 set의 API가 내장되어 있다
