# 리스트를 만들어 보자
# 평범하게 만들지 말고 배웠던 거 쓰면서 스펙타클하게
list = [1, 2]
list.append(3)
# [1, 2, 3]

list += [4]
# [1, 2, 3, 4]

list[0:-1] = [1, 2, 3]
# [1, 2, 3, 4]

# 일단 처음 볼 건 정렬 메소드
# 지금 리스트는 정렬돼 있지 않으니까 좀 섞어보자
list.clear()
list = [4, 1, 2, 5]
# 정렬은 sort
list.sort()

# 내림차순 정렬은 reverse에 True를 넘겨주면 된다
list.sort(reverse=True)
print(list)

# 그냥 reverse 메소드는 리스트 뒤집기
list.reverse()
print(list)

# 본격적으로 보자
print(list.index(4))
# 4라는 값이 처음 등장하는 곳의 위치를 리턴

list.insert(0, 8)
# 0번째 인덱스에 8 삽입

list.remove(8)
# 처음으로 나오는 8을 삭제

print(list.pop())
# 리스트 맨 마지막 값을 삭제하며 리턴

print(list.count(4))
# 리스트에 4라는 값이 몇개 있는지 세서 리턴
