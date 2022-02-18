# Create a sales report in xlsx which will have the following data.
# Sales Person 1 : 78,000.0
# Sales Person 2 : 32,000.0
# Sales Person 3 : 45,000.0
# Sales Person 4 : 11,000.0
# Sales Person 5 : 20,000.0
# Create a Pie Chart with the above data.

import xlsxwriter

workbook = xlsxwriter.Workbook('report_sales.xlsx')

worksheet = workbook.add_worksheet()

data_str = ['SalesPerson1', 'SalesPerson2', 'SalesPerson3', 'SalesPerson4', 'SalesPerson5']
data =[78000.0, 32000.0, 45000.0, 11000.0, 20000.0 ]
worksheet.write('A1', 'sales person')
worksheet.write('B1', 'salary')
worksheet.write_column('A2', data_str)
worksheet.write_column('B2', data)


chart = workbook.add_chart({'type': 'pie'})

chart.add_series({
    'name': ['Sheet1', 0, 1],
    'categories':
        ['Sheet1', 1, 0, 5, 0],
    'values': ['Sheet1', 1, 1, 5, 1]
})



chart.set_title({'name': 'Sales Report'})

worksheet.insert_chart('B9', chart)
workbook.close()