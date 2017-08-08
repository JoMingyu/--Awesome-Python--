# 빌트인 함수를 알아보자. 진짜 엄청 많다
# 일단 항상 써왔던 빌트인 함수는
print(type('hello'))
# 그리고 타입 캐스팅, input 그런것들

# 먼저 iterable data들에게 적용 가능한 빌트인들을 알아보자
lst = [3, 2, 1, 4]
print(all(lst))
# 요소가 모두 참이면 True

print(any(lst))
# 요소 중 하나라도 참이면 True

for index, num in enumerate(lst):
    # iterable data를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
    print(index, num)

print(len(lst))
# 요소의 전체 개수 리턴

print(max(lst))
print(min(lst))
print(sorted(lst))

# 더 많은 빌트인을 원한다면, builtins.py를 뒤져보자!
