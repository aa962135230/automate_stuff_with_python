import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))

print(wb.sheetnames)
sheet = wb['Sheet3']
print(sheet)
print(sheet.title)
another_sheet = wb.active
print(another_sheet)