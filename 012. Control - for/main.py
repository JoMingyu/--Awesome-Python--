# 파이썬에서 for문 진짜 짱 많이 쓴다
# 파이썬의 for문은 iteration 개념을 중요하게 생각한다
# 기본적으로 순회 방식을 띤다
lst = [1, 2, 3, 4]
for i in lst:
    print(i)

# 빌트인 함수 중 range라는 게 있다
for i in range(0, 5):
    print(i)
# range(n, m) -> n부터 m-1

for i in range(5):
    print(i)
# range(n) -> 0부터 n-1

# 좀 신기하게 for문을 돌릴 수 있다
lst = [(1, 2), (3, 4), (5, 6)]
for (first, second) in lst:
    print(first, second)
