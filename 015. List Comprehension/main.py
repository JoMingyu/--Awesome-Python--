# 리스트를 [2, 4, 6, 8] 과 같은 식으로 만들어야 될 때도 있을 것이다
# 리스트를 만드는 부분 자체를 for문으로 대체할 수 있다
# List Comprehension이라고 부른다

lst = [i for i in range(10)]
# 집합의 표현방법 중 조건제시법과 같다
# {i | i는 0부터 10 미만의 정수}
print(lst)

# 연산자를 넣어 보자
lst = [i * 2 for i in range(1, 11)]
print(lst)

# if문도 적용된다
lst = [i for i in range(100) if i % 3 == 0]
# {i | i는 0부터 100 미만의 정수 중 3의 배수}
print(lst)

# for문을 중첩할 수도 있다
# 2중 for문과 같다
lst = [i * j for i in range(2, 10)
       for j in range(1, 10)]
print(lst)
