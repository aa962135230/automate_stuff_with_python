import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

#create some data in column A
for i in range(1, 11):
    sheet['A' + str(i)] = i

ref_obj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
series_obj = openpyxl.chart.Series(ref_obj, title='First series')

chart_obj = openpyxl.chart.BarChart()
chart_obj.title = 'My Chart'
chart_obj.append(series_obj)

sheet.add_chart(chart_obj, 'C5')
wb.save('sampleChart.xlsx')