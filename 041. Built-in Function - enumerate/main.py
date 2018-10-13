# enumerate 함수는 iterable을 인덱스 기반으로 반복할 때 유용하게 사용된다

l = [1, 2, 3, 4, 5]
# iterable의 요소를 인덱스와 함께 순회해야 할 경우, 아래처럼 작성할 수 있다
for idx in range(len(l)):
    print(idx, l[idx])

# 코드는 정상적으로 실행되고, 원하던 결과값을 출력하고 있지만 enumerate() 함수를 통해 이를 조금 더 쉽게 표현할 수 있다

# -- enumerate(iterable[, start]) -> iterator for index, value of iterable(iterator)
for idx, item in enumerate(l):
    # (index, item)으로 이루어진 튜플로 이루어진 반복자(iterator)를 반환한다
    # [(index, item), (index, item), ...]와 유사한 모습이라 생각하면 된다
    print(idx, item)

for idx, item in enumerate(l, 3):
    # 순회할 iterable 객체의 start index를 설정해줄 수 있다
    print(idx, item)
