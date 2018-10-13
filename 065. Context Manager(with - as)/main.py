# 특정 객체들은 context(문맥)을 가진다
# 에를 들어, file 객체는 open - close의 2가지 context를 가진다

f = open('some.txt', 'w')
f.write('Hello')
f.close()

# Context Manager는 원하는 타이밍에 정확하게 리소스를 할당하고 제거하는 역할을 하는데
# 가장 많이 사용되는 Context Manager는 with - as문이다
with open('some.txt', 'w') as f:
    f.write('Hello')

# with 문에 의해 감싸진 객체는, entry point에서 __enter__()가 호출되며 as [obj]의 obj에 반환값을 할당하며
# exit point에서 객체의 __exit__()이 호출된다
# 파일 객체는 __enter__()에서 파일 객체를 열어 반환하고, __exit__()에서 파일 객체를 닫는 역할을 하므로 Context Manageable하다
# 따라서 매직 메소드 __enter__()와 __exit__()이 정의되어 있는 객체는 모두 Context Manageable하며, 'Context Manager 프로토콜을 구현하고 있다'라고 말한다

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
