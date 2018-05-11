# https://github.com/python-excel/xlwt
# pip install xlwt
from xlwt import Workbook
# xlrd를 만든 python-excel organization이 만든 라이브러리로
# Microsoft Excel 버전 95 ~ 2003과 호환되는 스프레드시트 파일을 생성하는 데 사용할 수 있음
# 표준 Python 배포판 외의 모듈이나 패키지에 의존하지 않는 pure python

wb = Workbook()
# Workbook 생성

ws = wb.add_sheet('Test')
# Worksheet 생성

ws.write(0, 0, 1)
ws.write(1, 0, 1.55)
ws.write(2, 0, 'Hi')
# ws.write(r, c, value)
# r행 c열에 value를 삽입

wb.save('test.xls')