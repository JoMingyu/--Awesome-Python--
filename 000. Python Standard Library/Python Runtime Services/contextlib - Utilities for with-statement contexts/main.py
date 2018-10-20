# https://docs.python.org/3/library/contextlib.html
import contextlib
# with 문과 관련된 작업을 위한 유틸리티를 제공한다
# 일반적으로 context manager 프로토콜을 구현하는 경우,
# __enter__와 __exit__ 메소드가 구현된 클래스를 정의하는 것이 일반적인데
# contextlib은 이러한 번거로움을 줄여준다
import csv

@contextlib.contextmanager
# with statement를 사용할 수 있는 context manager를
# generator 함수 형태로 정의할 수 있도록 돕는 데코레이터
def csv_file_reader(filename):
    file = open(filename)
    reader = csv.reader(file)

    try:
        yield reader
    finally:
        file.close()

# contextmanager에 데코레이팅된 함수는 호출되었을 때 generator를 반환해야 하며
# 위처럼 하나의 값만을 yield해야 한다
# yield된 값은 with statement에서 as 절에 명시한 대상에 바인드된다

with csv_file_reader('temp.csv') as reader:
    for r in reader:
        print(', '.join(r))
