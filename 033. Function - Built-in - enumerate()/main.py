l = [1, 2, 3, 4, 5]
# List의 요소를 인덱스와 함께 순회해야 할 경우, 아래처럼 작성할 수 있다
for idx in range(len(l)):
    print(idx, l[idx])

# 코드는 정상적으로 실행되고, 원하던 결과값을 출력하고 있지만 enumerate() 함수를 통해 이를 조금 더 쉽게 표현할 수 있다
for idx, item in enumerate(l):
    # (index, item)으로 이루어진 튜플로 이루어진 Iterator를 반환한다
    # [(index, item), (index, item), ...] 형태의 리스트라 이해해도 괜찮다
    print(idx, item)