# 빌트인 함수 zip()을 이용해 둘 이상의 iterable 객체를 한 번에 순회할 수 있다
for first, second in zip([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]):
    print(first, second)

# zip()은 전달된 iterable 객체들을 순회하다, 어느 iterable 객체든 더 이상 참조할 요소가 없으면 반복을 종료한다(짧은 iterable 객체 기준)
for first, second in zip([1, 2, 3, 4, 5], [2, 1]):
    print(first, second)

# 긴 iterable 객체를 기준으로 순회하려면 functools.zip_longest()를 사용하면 된다