# Create a medals report in xlsx for olympics based on countries as shown below.
# Country, Gold, Silver, Bronze, Total
# Country 1, 15, 20, 25, 60
# Country 2, 8,15,10, 33
# Country 3, 12,25,10, 47
# Country 4, 21,12,13, 50
# Country 5, 18,29,30, 77
# Create a Column chart with 3 medals gold, silver and bronze data.
# Create another Line chart with only total medals data

import xlsxwriter
workbook=xlsxwriter.Workbook('medal_report.xlsx')
worksheet=workbook.add_worksheet()

Title=['Country', 'Gold', 'Silver', 'Bronze', 'Total']
data1=['india', 15, 20, 25, 60]
data2=['australia', 8, 15, 10, 33]
data3=['sri lanka ', 12, 25, 10, 47]
data4=['New zealand', 21, 12, 13, 50]
data5=['South africa', 18, 29, 30, 77]

worksheet.write_row('A1',Title)
worksheet.write_row('A2',data1)
worksheet.write_row('A3',data2)
worksheet.write_row('A4',data3)
worksheet.write_row('A5',data4)
worksheet.write_row('A6',data5)

chart = workbook.add_chart({'type': 'column'})
chart.add_series({
    'name': ['Sheet1', 0, 1],
    'categories': ['Sheet1', 1, 0, 5, 0],
    'values': ['Sheet1', 1, 1, 5, 1]
})
chart.add_series({
    'name': ['Sheet1', 0, 2],
    'values': ['Sheet1', 1, 2, 5, 2]
})
chart.add_series({
    'name': ['Sheet1', 0, 3],
    'values': ['Sheet1', 1, 3, 5, 3]
})
chart.set_title({'name': 'Medal Report'})

worksheet.insert_chart('C11', chart)

chart1= workbook.add_chart({'type': 'line'})

chart1.add_series({
    'name': ['Sheet1', 0, 4],
    'categories': ['Sheet1', 1, 0, 5, 0],
    'values': ['Sheet1', 1, 4, 5, 4]
})
chart1.set_title({'name': 'Medal Total Report'})
worksheet.insert_chart('K11', chart1)


workbook.close()

