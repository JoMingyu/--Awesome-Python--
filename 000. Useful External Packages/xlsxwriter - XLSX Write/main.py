# https://github.com/jmcnamara/XlsxWriter
# pip install xlsxwriter
from xlsxwriter import Workbook
# pyexcelerate보다 느리지만 문서가 굉장히 잘 되어 있고
# xlwt보다 느리지만 xlsx write를 지원한다

wb = Workbook('Test.xlsx')
# Workbook 클래스의 인스턴스
# 인자로 파일 이름을 넘겨줄 수 있음

sheet = wb.add_worksheet('Test sheet')
# worksheet 추가

sheet.write('C5', 'hello')
# 엑셀에서 보편적으로 사용하는 (Column + row) 형태로 write

data = [
    (1, 'a'),
    (2, 'b'),
    (3, 'c')
]
# write를 위한 데이터

for idx, (left, right) in enumerate(data):
    sheet.write(idx, 0, left)
    sheet.write(idx, 1, right)
    # row index, column index를 이용한 write
    # write(row, column, data)

sheet.insert_image('B5', '')
# 이미지 insert 등 헬퍼 메소드들을 많이 가지고 있다

wb.close()
