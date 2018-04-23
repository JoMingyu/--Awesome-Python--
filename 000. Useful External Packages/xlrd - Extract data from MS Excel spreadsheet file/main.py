# https://github.com/python-excel/xlrd
# pip install xlrd
import xlrd
# xlrd는 only read를 목적으로만 하며, openpyxl이 읽지 못하는 .xls 파일도 읽을 수 있다
# 인지도 있는 엑셀 라이브러리들 중 read 속도가 가장 빠른 편에 속한다

wb = xlrd.open_workbook('test.xls')
# Workbook open
ws = wb.sheet_by_index(0)
# Worksheet load

print(ws.nrows)
# row 갯수
print(ws.ncols)
# column 갯수

print(ws.row_values(3))
# 3행의 모든 데이터를 list로 리턴
print(ws.col_values(5))
# 5열의 모든 데이터를 list로 리턴
print(ws.cell_value(3, 4))
# 3행 4열의 데이터를 리턴
