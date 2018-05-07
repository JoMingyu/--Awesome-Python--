# 매직 메소드(Magic Method)를 정의하기 위해서도 언더스코어를 사용한다
# 두 개의 언더스코어로 시작하고, 종료되는 메소드를 매직 메소드라고 부른다
# __init__, __len__, __str__ 등
# 이들은 보통 파이썬 인터프리터에 간접적으로 호출된다(len(obj) 호출 시 obj.__len__() 호출, str(obj) 호출 시 obj.__str__() 호출 등)
l = [1, 2, 3, 4, 5]

print(len(l))
print(l.__len__())

print(str(l))
print(l.__str__())