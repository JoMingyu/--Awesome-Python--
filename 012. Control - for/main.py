# 파이썬은 Iterable 객체에 대한 서포트가 많다 보니 for문이 애초에 for-each 형태(참조 방식)로 만들어져 있다
# 순차 참조 방식을 띤다
lst = [1, 2, 3, 4]
for i in lst:
    print(i)

# 빌트인 함수 중 range라는 게 있다. range(n, m)은 n부터 m-1 사이의 정수 리스트를 만든다
for i in range(0, 5):
    print(i)

for i in range(5):
    print(i)
# range(n) -> 0부터 n-1

# 리스트 안에 튜플을 넣어 보자. 리스트에서 잠깐 했었던 Unpack 덕분에 좀 신기하게 for문을 돌릴 수 있다
lst = [(1, 2), (3, 4), (5, 6)]
for first, second in lst:
    print(first, second)
