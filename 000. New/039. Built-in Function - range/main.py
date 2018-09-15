# 빌트인 함수 range를 통해 iterable인 range객체를 얻어올 수 있으며, for문에 자주 사용된다

# -- range(stop) -> range object for 0~stop-1(iterable)
# -- range(start, stop[, step=1]) -> range object for start~stop-1 jumped by step(iterable)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(n) -> 0부터 n-1까지의 Sequence를 반환

print(list(range(5, 10))) # [5, 6, 7, 8, 9]
# range(n, m) -> n부터 m-1까지의 Sequence를 반환

print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]
# range(n, m, step)은 n부터 m-1까지의 수를 step만큼 더해가며 요소화한 Sequence를 반환

for i in range(10):
    # range 객체는 iterable이므로 for문에 사용 가능
    print(i)
