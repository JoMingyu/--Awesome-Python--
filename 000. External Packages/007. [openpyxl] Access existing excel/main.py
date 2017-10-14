# xlsxwriter는 데이터 write만 가능했다. 이미 존재하는 엑셀 파일을 읽을 필요가 있다면 openpyxl을 사용하자
# pip install openpyxl

from openpyxl import load_workbook

wb = load_workbook('test.xlsx')
sheet = wb['test_sheet']

print(sheet['A1'].value)
sheet['A2'] = 'New Data'

wb.save('test.xlsx')
