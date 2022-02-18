# 2.Create a student report in xlsx which will have 4 columns student, maths, science,english 3 subjects marks. Now create a line chart for this data in xlsx.

import xlsxwriter

workbook = xlsxwriter.Workbook('student_report.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1','Student')
worksheet.write('B1','Maths')
worksheet.write('C1','Science')
worksheet.write('D1','English')


chart=workbook.add_chart({'type':'line'})
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

worksheet.insert_chart('A7', chart)
chart.set_title({'name': 'Student Marks'})

data_name = ['inam','husain','abid']
data_str2 = [99,50,40.985516651]
data_str3 = [20,40,60]
data_str4 = [85,87,74]



worksheet.write_column('A2',data_name)
worksheet.write_column('B2',data_str2)
worksheet.write_column('C2',data_str3)
worksheet.write_column('D2',data_str4)

workbook.close()





