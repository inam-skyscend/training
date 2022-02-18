import xlrd

workbook=xlrd.open_workbook("EmployeeData.xls")
worksheet=workbook.sheet_by_index(0)

f_row=[]
for col in range(worksheet.ncols):
    f_row.append(worksheet.cell_value(0,col))
print(f_row)

detail=[]
for row in range(1,worksheet.nrows):
    data={}
    for col in range(worksheet.ncols):
        data[f_row[col]]=worksheet.cell_value(row,col)
    detail.append(data)
print(detail)
