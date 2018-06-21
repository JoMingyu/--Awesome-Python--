# 함수의 인자 중 키워드 인자는 위치 인자처럼 넘겨줄 수도 있고, 인자의 이름을 명시하여 넘겨줄 수도 있었다
def sum(a=0, b=0):
    return a + b

print(sum(1, 3))
print(sum(a=1, b=3))

# 키워드 인자를 강제하여 명시성을 강조할 수도 있는데, 이를 키워드 전용 인자라고 부르며 asterisk(*) 뒤에 인자를 명시하면 된다
def sum(*, a=0, b=0):
    return a + b

print(sum(1, 3))
# TypeError: sum() takes 0 positional arguments but 2 were given
print(sum(a=1, b=3))
# 4