# with-as 문은 파이썬 2.5에서 도입된 기능
# 객체 사용 전과 후에 꼭 해줘야 하는 것들을 줄이는 일을 with-as 문으로 해결할 수 있다
# 객체에는 인터프리터의 context manager에 의해서 실행되는 __enter__()와 __exit__() 메소드가 정의되어 있어야 with-as문을 적용할 수 있다

# 파이썬의 file 객체는 __enter__와 __exit__ 함수가 구현되어 있다. 각각 file object 객체 자신을 리턴하고, 후자는 file을 닫아준다
with open('test.txt', 'w') as f:
    # open()시 리턴되는 파일 객체가 with을 만나 __enter__()를 호출
    # 파일 객체의 __enter__() 메소드의 리턴 값이 f로 사용됨. 여기서는 파일 객체 자신
    f.write('hello')
    # with 블럭이 종료되며 __exit__() 호출
    # 여기서는 파일 객체를 닫아줌(f.close())
