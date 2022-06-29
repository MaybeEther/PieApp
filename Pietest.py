import matplotlib.pyplot as plt
import numpy as np
import xlrd

temp = ("test.xlsx")
#wb = xlrd.open_workbook(temp)

#sheet = wb.sheet_by_index(0)
#sheet.cell_value(0, 0)
#for i in range(sheet.ncols):
    #print(sheet.cell_value(0, i))
y = np.array([35, 25, 25, 15])
mycolors = ["black", "w", "b", "#4CAF50"]
plt.pie(y)
plt.show()