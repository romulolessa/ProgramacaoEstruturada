import pandas as pd
import matplotlib.pyplot as plt
import xlrd

x = pd.read_excel(r'C:\Users\JAVA\Desktop\premios.xlsx')
plt.pie (x['Valor'] , labels = x['ID'] , autopct = '%1.2f%%')
plt.show()