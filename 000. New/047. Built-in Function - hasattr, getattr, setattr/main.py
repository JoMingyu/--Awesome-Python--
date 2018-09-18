# Python에서 객체의 속성은 dynamic해서, 불확실성이 존재하기 때문에 객체의 속성에 접근하는 것은 unsafe하다.
# 객체에 어떤 속성이 있는지를 검사하거나, 어떤 속성에 안전하게 접근(있으면 값을 반환, 없으면 기본값 반환)하기 위해
# hasattr, getattr, setattr 함수가 존재한다
# in 연산자로 검사할 수 있지 않나 싶겠지만, in은 iterable이 아닌 객체에는 사용 불가능하다

# -- hasattr(obj, name) -> bool
# obj에 name이라는 속성이 존재하는지를 bool로 반환한다
print(hasattr([], 'append')) # True
print(hasattr([], 'get')) # False

# -- getattr(obj, name[, default]) -> value
# obj에서 name이라는 속성에 할당된 값을 반환한다
print(getattr([], 'count')(3)) # 0
# []라는 리스트에서 count 속성을 가져오고, 이는 메소드기 때문에 즉시 호출
# 그러나 default가 없는 경우 getattr(obj, name)은 obj.name과 동일한 역할이며,
# 따라서 getattr은 대부분 default value를 전달하여 safe get을 보장하기 위해 사용한다
print(getattr([1, 2, 3], '__len__', lambda: 0)()) # 0
# [1, 2, 3] 리스트에서 __len__ 속성을 가져오고, 존재하지 않는다면 default인 'lambda: 0'을 반환

# -- setattr(obj, name, value)
# obj의 name 속성에 value를 할당한다
class C: pass

c = C()
setattr(c, 'useless_attr', 10)

print(c.useless_attr) # 10
# setattr(obj, name, value)는 obj.name = value와 동일해서, hasattr이나 getattr만큼 자주 사용되진 않는다
