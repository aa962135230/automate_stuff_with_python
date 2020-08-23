import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24_font = Font(size=24, italic=True)

sheet['A1'].font = italic24_font
sheet['A1'] = 'Hello world!'
wb.save("styled.xlsx")
