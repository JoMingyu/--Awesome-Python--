# 리스트를 [2, 4, 6, 8] 이런 식으로 만들어야 될 때도 있을 것이다
# for문을 돌릴 수도 있지만 리스트를 for로 만들 수 있다(?)
# List Comprehension이라고 부른다
lst = [i for i in range(10)]
print(lst)

# 좀 복잡하게도 된다
lst = [i * 2 for i in range(1, 11)]
# 1부터 10까지의 range에 2를 곱합
print(lst)

# if문도 적용된다
lst = [i for i in range(100) if i % 3 == 0]
print(lst)

# for문을 여러개 사용할 수도 있다
lst = [i * j for i in range(2, 10)
       for j in range(1, 10)]
print(lst)
