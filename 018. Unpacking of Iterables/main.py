# Iterable의 예제에서 봤던, 컬렉션을 변수에 대입하는 표현식을 packing이라고 부른다

l = [1, 2, 3, 4, 5]

# 반대로, 컬렉션의 데이터를 여러 변수에 나눠담는 것을 unpacking이라고 부른다(destructuring이라고도 함)
a, b, c = [1, 2, 3]
print(a) # 1
print(b) # 2
# 우변의 데이터와 좌변의 변수를 각 자리에 맞게 바인딩

# a, b, c = [1, 2, 3, 4]
# 대입문 양 변의 길이가 다르면 오류가 발생한다
# Python 3에선, 대입문에서 좌변의 변수 중 하나에 asterisk(*)을 붙이면 다른 변수에 대입하고 남은 전체를 리스트로 담을 수 있다
a, b, *rest = [1, 2, 3, 4]
print(rest) # [3, 4]
a, *rest, b = (1, 2, 3, 4, 5)
print(rest) # [2, 3, 4]
# unpacking에 사용된 컨테이너 객체의 타입에 관계없이, list로 반환

# unpacking은 변수의 swap에서 유용하게 사용된다
a, b = 1, 2
a, b = b, a
print(a) # 2
print(b) # 1
