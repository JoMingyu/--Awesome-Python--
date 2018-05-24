# del statement를 사용하면, local namespace 또는 global namespace에서 해당 이름의 바인딩이 제거된다
l = [1, 2, 3, 4, 5]
del l[1]

print(l)
# [1, 3, 4, 5]