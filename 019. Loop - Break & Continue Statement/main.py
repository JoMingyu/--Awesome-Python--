# break와 continue statement는 반복문에서 사용 가능하며
# 반복문을 더 세부적으로 조작하기 위해 사용한다

# -- break
# 반복문을 종료하고, 해당 반복문 블럭 밖으로 탈출한다
for key, value in {1: 10, 2: 20, 3: 30}.items():
    print('Searching, current key is {}'.format(key))
    if value == 20:
        print('20 Fonud! key is {}'.format(key))
        break

count = 0
while True:
    print('Currnet count is {}'.format(count))
    count += 1

    if count == 10:
        break

# -- continue
# continue 뒤의 코드를 실행하지 않고, 다음 반복으로 제어를 넘긴다
for i in [1, 2, -3, 4, -5, 6]:
    if i < 0:
        continue
    print(i)