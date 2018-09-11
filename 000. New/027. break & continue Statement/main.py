# break와 continue statement는 for, while과 같은 반복문의 내부에서 사용 가능하며
# 자연스러운 반복의 흐름 중간에, 제어를 의도적으로 조작하기 위하여 사용됨

# -- break
# 반복문을 종료하고, 해당 반복문 블럭 밖으로 탈출한다
for item in [1, 3, 6, 17, 38, 20, 93]:
    print('Searching, current item is {}'.format(item))
    if item == 20:
        print('20 Fonud!')
        break

count = 0
while True:
    print('Currnet count is {}'.format(count))
    count += 1

    if count == 10:
        break

# -- continue
# 즉시 다음 반복으로 제어를 넘긴다
for i in [1, 2, -3, 4, -5, 6]:
    if i < 0:
        continue
    print(i)
