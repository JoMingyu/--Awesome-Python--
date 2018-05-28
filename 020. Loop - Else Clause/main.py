# Python에서는 반복문에 else clause를 명시할 수 있다
# 반복문이 중간에 break되지 않고 정상적으로 종료되면 else 블럭의 코드가 실행된다
for i in [1, 2, 3, 4, 5]:
    if i > 10:
        break
else:
    print('The for loop was terminated normally')
    # 출력됨

while True:
    break
else:
    print('The while loop was terminated normally')
    # 출력되지 않음