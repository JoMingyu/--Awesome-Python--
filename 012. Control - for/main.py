# 파이썬에서 for문 진짜 짱 많이 쓴다
# 파이썬의 for문은 iteration 개념을 중요하게 생각한다
# 기본적으로 순회 방식을 띤다
lst = [1, 2, 3, 4]
for i in lst:
    print(i)
# 실행 과정
# 1. lst의 첫 번째 원소인 1이 i에 대입되어 for문 블록 내에 있는 작업을 수행한다
# 2. lst의 두 번째 원소인 2가 i에 대입되어 for문 블록 내에 있는 작업을 수행한다
# 3. lst의 세 번재 원소인 3이 i에 대입되어 for문 블록 내에 있는 작업을 수행한다
# 4. lst의 네 번째 원소인 4가 i에 대입되어 for분 블록 내에 있는 작업을 수행한다
# 5. lst내에 있는 모든 원소에 대해 작업이 끝났기에 for문을 끝낸다

# 빌트인 함수 중 range라는 게 있다
for i in range(0, 5):
    print(i)
# range(n, m) -> n부터 m-1 까지의 iterator를 반환해준다

for i in range(5):
    print(i)
# range(n) -> 0부터 n-1

# 좀 신기하게 for문을 돌릴 수 있다
lst = [(1, 2), (3, 4), (5, 6)]
for (first, second) in lst:
    print(first, second)
