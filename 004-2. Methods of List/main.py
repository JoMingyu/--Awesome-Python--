# 리스트를 만들어 보자
_list = [1, 2, 3]

_list += 4,
# 길이가 1인 tuple로 붙이기
# [1, 2, 3, 4]

_list[0:-1] = [1, 2, 3]
# [1, 2, 3, 4]

# 처음 볼 건 정렬 메소드
# 지금 리스트는 정렬돼 있지 않으니까 좀 섞어보자
_list.clear()
_list = [4, 1, 2, 5]
# 정렬은 sort
_list.sort()

# 내림차순 정렬은 reverse에 True를 넘겨주면 된다
_list.sort(reverse=True)
print(_list)

# 그냥 reverse 메소드는 리스트 뒤집기
_list.reverse()
print(_list)

print(_list.index(4))
# 4라는 값이 처음 등장하는 곳의 위치를 리턴

_list.insert(0, 8)
# 0번째 인덱스에 8 삽입

_list.remove(8)
# 처음으로 나오는 8을 삭제
# del _list[_list.index(8)]보다 더 좋은 구문이다

print(_list.pop())
# 리스트 맨 마지막 값을 삭제하며 리턴

print(_list.count(4))
# 리스트에 4라는 값이 몇개 있는지 세서 리턴
# 요소 카운팅은 자주 쓰인다
