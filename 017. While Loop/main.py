# While은 특정 조건에 충족하는 경우 동일한 코드를 반복해서 수행하기 위해 사용한다
# Python에는 do-while이 존재하지 않는다
count = 0

# while [condition]
while count < 10:
    print('Current count : {}'.format(count))
    count += 1