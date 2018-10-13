# Python은 글로벌 네임스페이스 수준에서 지원되는 함수들이 있고, print 함수가 그들 중 하나

# -- type(object) -> the object's type
# type 함수는 타입에 관계없이 하나의 객체를 인자로 전달받아, 해당 객체의 타입을 <class 'type'> 형태로 반환
# 새로운 타입을 만들 때도 사용하나, 현재 레벨에선 설명 생략
print(type(1)) # <class 'int'>
print(type('')) # <class 'str'>
print(type([])) # <class 'list'>
print(type({})) # <class 'dict'>
print(type(lambda: None)) # <class 'function'>
# 디버깅 시 자주 사용된다

# -- Type Casting Functions
# 빌트인 타입들은 그들에 대응되는 빌트인 함수가 있다(정확히는 해당 타입에 대한 생성자)
# 이들은 인자의 전달 여부에 따라 해당 타입의 false value(0, '', [], {} 등)를 반환받거나,
# 타입 캐스팅에 활용된다
print(int()) # 0
print(int('123')) # 123
# int(x=0)
print(str(15.89)) # '15.89'
# str(object='')

print(list('hi')) # ['h', 'i']
# list() 혹은 list(iterable)
# print(dict([1, 2])) # error
print(dict([(1, 2), (3, 4)])) # {1: 2, 3: 4}
# dict() 혹은 dict(nested iterable)
# 모든 빌트인 iterable 객체들은 서로 캐스팅이 가능하다(프로토콜만 맞춰 준다면)
# 예를 들어, dict는 길이가 2인 iterable로 이루어진 iterable을 딕셔너리로 만들어 준다
