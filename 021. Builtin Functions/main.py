# 수많은 빌트인 함수들 중 자주 쓰는 것들을 알아보자
# 파이썬3의 빌트인 함수들은 아래에서 찾아볼 수 있다
# https://docs.python.org/3/library/functions.html
# 아니면 builtins.py를 뒤져봐도 될 것 같다

# 그동안 자주 써봤던 빌트인 함수는 type
print(type('hello'))
# 그리고 타입 캐스팅, input 등
print(int('2'))

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
# 요소의 전체 개수
print(max(lst))
# 최대값
print(min(lst))
# 최소값
print(sorted(lst))
# 정렬된 리스트