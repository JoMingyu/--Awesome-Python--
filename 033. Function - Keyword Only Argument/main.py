# 함수에 인자를 전달하는 경우, 위치 인자로 전달할 수도 있고 키워드 인자로 전달할 수도 있다

def sum(a, b):
    return a + b

print(sum(1, 3)) # 4
print(sum(a=1, b=3)) # 4

# 키워드 인자를 강제하여 명시성을 강조할 수도 있는데,
# 이를 키워드 전용 인자라고 부르며 asterisk(*) 뒤에 인자들을 명시하면 된다
def sum(*, a, b=0):
    return a + b

print(sum(1, 3))
# TypeError: sum() takes 0 positional arguments but 2 were given
# 위치 인자로 전달하면 에러 발생
print(sum(a=3)) # 3

# https://velog.io/@city7310/Positional-Only-Keyword-Only-Arguments-k9jv9u0tmz
