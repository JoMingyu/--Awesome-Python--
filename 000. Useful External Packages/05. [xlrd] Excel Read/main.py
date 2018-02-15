# pip install xlrd
import xlrd
# openpyxl은 .xls 파일을 읽지 못한다
# xlrd는 only read를 목적으로만 함
# 엑셀 Read에선 속도가 가장 빠른 듯 싶다

wb = xlrd.open_workbook('test.xls')
ws = wb.sheet_by_index(0)

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

