# 아래는 두 수를 더하는 함수
def _sum(x, y):
    return x + y

print(_sum(2, 4))

# lambda 표현으로는?
print((lambda x, y: x + y)(10, 20))
# 일단 함수를 간단화할 수 있다는 장점이 먼저 보인다
# lambda는 변수에 할당할 수 있는데, 선언식 lambda는 PEP8 표준에 어긋나므로 사용하지 말자
# f = lambda x: x + 5

# 함수적 프로그래밍 개념에선 매개변수로 함수를 전달하는 형태로 프로그래밍을 하는데
# 파이썬에선 lambda를 이용해 익명 함수를 만들 수 있으므로 이를 통해  함수적인 프로그래밍을 할 수 있다

# 빌트인 함수인 map과 lambda를 섞어 보자. map은 mapping이라는 단어를 떠올리면 된다
# map(함수, 리스트) 형태로, 리스트로부터 원소를 하나씩 꺼내 함수를 적용시킨 다음, 그 결과를 새로운 리스트에 담아 준다
# List Comprehension과 비슷해 보일 것이다
print(list(map(lambda x: x ** 2, range(5))))
# 똑같은 결과를 내보내는 List Comprehension
print([x ** 2 for x in range(5)])

# 이번엔 filter를 해 보자. 단어 그대로 filtering하는 역할을 해준다
print(list(filter(lambda x: x < 5, range(10))))

# 리스트를 만들어내는 건 Comprehension, 만들어진 리스트를 컨트롤하는건 lambda 방식이 적합한 것 같다
# 근데 람다는 반로썸 아저씨가 싫어한다. Comprehension으로 대체 가능하기 때문인 듯
