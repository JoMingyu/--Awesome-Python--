# 특정 객체들은 context(문맥)을 가진다
# 에를 들어, file 객체는 open - close의 2가지 context를 가진다

f = open('some.txt', 'w')
f.write('Hello')
f.close()

# Context Manager는 원하는 타이밍에 정확하게 리소스를 할당하고 제거하는 역할을 하는데
# 가장 많이 사용되는 Context Manager는 with - as문이다
with open('some.txt', 'w') as f:
    f.write('Hello')

# with 문은 entry point에서 전달된 객체의 __enter__()를 호출하며 해당 함수의 리턴을 `as [obj]`의 obj에 바인딩하고,
# exit point에서, exit의 사유가 어떻든 객체의 __exit__()을 호출한다
# 이러한 magic method들이 정의되어 있어, with문이 정상적으로 흐름을 관리할 수 있는 객체를 파이썬에선 context manager라고 부른다
# == 합당한 스펙의 __enter__()와 __exit__()이 정의되어 있는 객체는 context manageable하다

class File:
    def __init__(self, file_name, method='r'):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print('__enter__()')
        return self.file_obj

    def __exit__(self, type, value, trace_back):
        print('__exit__()')
        self.file_obj.close()

print('Before entry with - as')
with File('some.txt', 'w') as f:
    f.write('Hello')
    print('Before exit with - as')

print('Finished with - as')

# 위 코드는 아래와 같은 순서의 출력을 가진다
# Before entry with - as
# __enter__()
# Before exit with - as
# __exit__()
# Finished with - as
