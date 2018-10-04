# Unpacking은 함수에 인자를 전달하는 경우에도 사용할 수 있으며, 이를 Argument Unpacking이라고 부른다
# * 연산자(starred operator)을 사용하며, 이는 가변 인자 표현인 *args나 **kwargs와 동일한 원리이다

def sum(a, b, c, d):
    return a + b + c + d

print(sum(*[1, 2, 3, 4])) # 10

print(*[1, 2, 3, 4], sep='\n')
# print의 sep 파라미터와 argument unpacking을 응용하여 리스트의 요소를 개행으로 구분하여 출력

# ** 표현을 사용해 딕셔너리를 키워드 인자 형태로 전달할 수
def sum(x, y):
    return x + y

print(sum(**{'x': 1, 'y': 3})) # 4

# 위와 같은 특징 때문에, 문법적으로 지원되고 있지 않는 Tuple comprehension을 우회적으로 표현할 수도 있다
x = *[i for i in range(5)],
print(x) # (1, 2, 3, 4, 5)
