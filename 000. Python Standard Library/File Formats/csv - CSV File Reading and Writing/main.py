# https://docs.python.org/3/library/csv.html
import csv
# https://github.com/python/cpython/blob/3.6/Lib/csv.py
# CSV(Comma Separated Values)는 스프레드시트와 데이터베이스를 위한 가장 일반적인 import/export 포맷
# csv 모듈은 CSV 포맷의 데이터 read/write를 위한 클래스들이 구현되어 있다

with open('test.csv', 'w') as file:
    writer = csv.writer(file, delimiter=' ')
    # delimiter는 각 요소 간의 구분자(기본값은 ',')

    writer.writerow(['Spam'] * 5 + ['Bacon'])
    writer.writerow({'Spam', 'Ham', 'Beef'})
    writer.writerow({1: 3, 4: 5})
    # iterable 객체를 iteration하며 순차적으로 기록하기 때문에, iterable이라면 어느 객체를 전달해도 상관 없음

with open('test.csv') as file:
    reader = csv.reader(file, delimiter=' ')
    
    print(type(reader))
    # <class '_csv.reader'>

    print(dir(reader))
    # __iter__()를 구현하고 있는 iterable 객체

    for row in reader:
        # 따라서 reader 객체에 바로 for loop 가능

        print(row)
        # read는 언제나 list 타입으로 반환

        print(type(row[0]))
        # 요소들은 모두 문자열 타입