#coding:utf-8
import openpyxl

#rexcel = open_workbook("table.xls") # 用wlrd提供的方法读取一个excel文件
##rows = rexcel.sheets()[0].nrows # 用wlrd提供的方法获得现在已有的行数
#excel = copy(rexcel) # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
#table = excel.get_sheet(0) # 用xlwt对象的方法获得要操作的sheet
#values = ["1", "2", "3"]
#row = 1
#for value in values:
    #table.write(row, 0, value) # xlwt对象的写方法，参数分别是行、列、值
    #table.write(row, 1, "haha")
    #table.write(row, 2, "lala")
    #row += 1
#excel.save("table.xls")

wb=openpyxl.load_workbook('table.xlsx')
ws=wb['Sheet1']
ws.cell(row=1,column=1).value='8 9 7 6 6'
wb.save('table.xlsx')
