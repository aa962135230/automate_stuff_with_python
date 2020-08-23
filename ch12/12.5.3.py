import openpyxl

wb = openpyxl.Workbook()
sheet = wb['Sheet']
print("更新前A1值:", sheet['A1'].value )
sheet['A1'] = 'Hello world!'
print("更新后A1值:", sheet['A1'].value )
