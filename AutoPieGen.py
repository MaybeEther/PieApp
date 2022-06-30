import matplotlib.pyplot as plt
import numpy as np
import xlrd
##########################################
x = []
a = []
temp = ("test.xls") # file selecter
wb = xlrd.open_workbook(temp)
sheet = wb.sheet_by_index(0)

e = sheet.cell_value(1,0)
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
if isfloat(e):                         #for if the list goes accross colloms 
    sheet.cell_value(1, 0)
    for i in range(sheet.ncols):
        x.append(sheet.cell_value(1, i))
    sheet.cell_value(0, 0)
    for i in range(sheet.ncols):
        a.append(sheet.cell_value(0, i))
else:
    sheet.cell_value(0, 0)             #for if the list goes up and down rows
    for i in range(sheet.nrows):
        x.append(sheet.cell_value(i, 1))
    sheet.cell_value(0, 1)
    for i in range(sheet.nrows):
        a.append(sheet.cell_value(i, 0))

y = np.array(x)
plt.pie(y, labels=a)
plt.show()
