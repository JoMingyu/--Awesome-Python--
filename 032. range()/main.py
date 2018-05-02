# 빌트인 함수 range()를 통해 list와 같은 Iterable&Sequence인 range객체를 얻어올 수 있으며, for문에 자주 사용된다
print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(n)은 0부터 n-1까지의 Sequence를 반환

print(list(range(5, 10)))
# [5, 6, 7, 8, 9]
# range(n, m)은 n부터 m-1까지의 Sequence를 반환

print(list(range(0, 10, 2)))
# [0, 2, 4, 6, 8]
# range(n, m, step)은 n부터 m-1까지의 수를 step만큼 더해가며 요소화한 Sequence를 반환

for i in range(10):
    # range 객체는 iterable이므로 for문에 사용 가능
    print(i)