# with-as 문은 파이썬 2.5에서 도입된 기능
# 객체 사용 전과 후에 꼭 해줘야 하는 것들을 줄이는 일을 with-as 문으로 해결할 수 있다
# 객체에는 인터프리터의 context manager에 의해서 실행되는 __enter__()와 __exit__() 함수가 정의되어 있어야 한다.

# 파이썬의 file 객체는 __enter__와 __exit__ 함수가 구현되어 있다. 각자 file object 객체 자신을 리턴하고, 후자는 file을 닫아준다.
with open('test.txt', 'w') as f:
    # __enter__()의 리턴 값이 f로
    f.write('hello')
    # 블럭이 끝날 때 __exit__() 호출
