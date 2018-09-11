# Python의 for문은, 일반적인 언어의 for(인덱스 기반)와 달리 for-each 형태를 띤다

for i in [1, 2, 3, 4, 5]:
    # for [item] in [iterable]
    print(i)
# 리스트의 각 원소들이 반복을 기준으로 차례대로 i에 대입되며,
# 더이상 참조할 원소가 없을 때까지 블럭 내의 코드를 반복한다

# item은 여러 개가 될 수 있으며, 아래처럼 iterable의 각 요소가
# unpack 가능한 경우(갯수가 서로 맞는 경우)에는 자동으로 unpack되기도 한다
for v1, v2 in [[1, 2], [3, 4], [8, 9]]:
    print(v1, v2)
