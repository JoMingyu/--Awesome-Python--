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

# asterisk 뒤에 명시된 Keyword Only Argument들은 일반 argument와 다르게,
# non-required 인자가 required 인자 앞에 와도 문제가 없다
def f1(*, a=0, b): # keyword only argument들은 required 여부에 상관 없이 나열 가능
    pass

def f2(a=0, b): # 일반 argument들은 required argument가 non-required argument 앞에 와야만 함
    pass

# Python 3.8부터는 Positional Only Argument를 사용할 수 있다

def sum(/, a, b):
    return a + b

print(sum(1, 3))


# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#        |              |                 |
#        |        Positional or keyword   |
#        |                              Keyword only
#     Positional only

# https://velog.io/@city7310/Positional-Only-Keyword-Only-Arguments-k9jv9u0tmz
