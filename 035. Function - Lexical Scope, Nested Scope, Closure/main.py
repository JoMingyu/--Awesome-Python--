# -- Lexical Scope, Nested Scope
# Scope가 생기는 시점에 따라, 언어의 스코핑 방식이 나뉜다
# -> 함수의 호출 시점에 생기면 동적 스코핑(호출할 때마다 스코프가 달라질 수 있음), 선언 시점에 생기면 정적 스코핑
# 대부분의 언어는 선언 시점에 스코프가 생기는 정적 스코핑 방식이 사용되고
# Python도 정적 스코핑, 또는 어휘적 스코핑(Lexical Scoping) 방식이 사용된다
def outer():
    n = 10
    def inner():
        print(n)
        # 내부 함수에서 외부 함수의 지역변수인 n에 참조
        # Lexical scoping 기반의 언어는, 내부에 중첩된 함수가 외부 함수의 네임스페이스에 접근할 권한을 가진다
        # -> 외부 네임스페이스가 아닌 외부 함수의 네임스페이스 접근이며, 외부 네임스페이스의 접근은 lexical scoping과 관련이 없음
    # 그러나 외부 함수는 내부 함수의 네임스페이스에 접근할 수 없다. 이를 nested scope라고 부른다

# -- Closure
def get_number_printer(n):
    def print_number():
        print(n)
    
    return print_number

func = get_number_printer(3)
func() # 3
# 지역변수 n을 가진 get_number_printer 함수는 print_number 함수를 반환하며 종료되었지만,
# 해당 함수의 반환 결과인 func 함수는 정상적으로 get_number_printer의 지역변수에 접근할 수 있음

# 함수가 호출되고 나면, 그 함수와 함수가 선언된 lexical scope에 대한 정보를 조합한 '클로저'가 형성된다
# 클로저의 lexical scope는 클로저가 생성된 시점의 범위 내에 있는 모든 지역 변수로 구성되기 때문에,
# 위의 경우에서 func는 get_number_printer가 실행될 때 생성된 클로저 중 하나인 print_number 함수에 대한 참조다
# 해당 참조는 자신과 동일한 클로저에 속해 있는 지역변수 n에 대한 참조를 유지한다
# 따라서 스코프 내의 영역은 소멸되었지만 클로저는 살아있기 때문에 외부 함수의 지역변수에 접근이 가능하다
