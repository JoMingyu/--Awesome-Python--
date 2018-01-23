# 자료형들이 참 많은데 빈 리스트나 빈 딕셔너리 같은거 만들 경우가 생각보다 많다
# 빌트인 함수를 쓰는 것과 리터럴을 이용해 선언하는 두 가지 방식이 있다
lst1 = list()
lst2 = []

dict1 = dict()
dict2 = {}

tuple1 = tuple()
tuple2 = ()
# 일단 비워 두고 나중에 요소를 추가하기 위해 iterable 객체를 생성하는 경우, 리터럴보다 빌트인을 써서 선언하는 것이 좋다(PEP8)

set1 = set()
# 빈 set을 리터럴로 선언 불가(딕셔너리와 구별할 수 없기 때문)

i = int()
i = 4

s = str()
s = '!'

f = float()
f = 3.5

# 아직 아무것도 할당되지 않은 변수는
none = None
# 자바에 null, JS에 undefined가 있는 것처럼 파이썬엔 None이 있다

print(type(none))
# <class 'NoneType'>
