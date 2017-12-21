# 파이썬은 Iterable 객체에 대한 서포트가 많다 보니 for문이 애초에 for-each 형태(참조 방식)로 만들어져 있다
# 순차 참조 방식을 띤다
lst = [1, 2, 3, 4]
for i in lst:
    print(i)
# 실행 과정
# 1. lst의 첫 번째 원소인 1이 i에 대입되어 for문 블록 내에 있는 작업을 수행한다
# 2. lst의 두 번째 원소인 2가 i에 대입되어 for문 블록 내에 있는 작업을 수행한다
# 3. lst의 세 번재 원소인 3이 i에 대입되어 for문 블록 내에 있는 작업을 수행한다
# 4. lst의 네 번째 원소인 4가 i에 대입되어 for분 블록 내에 있는 작업을 수행한다
# 5. lst내에 있는 모든 원소에 대해 작업이 끝났기에 for문을 끝낸다

# 빌트인 함수 중 range라는 게 있다. range(n, m)은 n부터 m-1 사이의 iterator를 반환해준다
for i in range(0, 5):
    print(i)

for i in range(5):
    print(i)
# range(n) -> 0부터 n-1

# 리스트 안에 튜플을 넣어 보자. 리스트에서 잠깐 했었던 Unpack 덕분에 좀 신기하게 for문을 돌릴 수 있다
lst = [(1, 2), (3, 4), (5, 6)]
for first, second in lst:
    print(first, second)

# 파이썬에는 for문에도 else를 쓸 수 있다
for i in range(10):
    print(i)
else:
    print('Success')
# 루프 본문이 break문을 만나지 않은 경우에만 else 블록이 실행된다
# Effective Python에서는 직관적이지 않고 혼동하기 쉬우니 사용하지 않는 것이 좋다고 한다

for i in range(10):
    print(i)
    if i == 5:
        print('Fail')
        break
else:
    print('success')
# for문 내에서 break에 걸리지 않고 온전하게 for문을 마치면 else문 블럭 내에 작업을 수행한다