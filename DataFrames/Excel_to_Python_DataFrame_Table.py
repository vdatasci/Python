#Excel to Python Conversion:
import pandas as pd
import numpy as np


df = pd.read_excel("C:\\Users\\Linda\\Downloads\\Ginzberg.csv")
df.head()

list(df.columns.values)

df.Product
df.iloc[:,:2]
df.iloc[:3]

df[(df['Price'] > 500) | (df['Price'] < 50)]
df[~(df['Account'] == '714466')]

df.sample(n=3)
df.sample(frac=0.5)
df.where(Price <= 10000)

#Pivot Table:
sales_report = pd.pivot_table(df, index=["Manager", "Rep", "Product"], values=["Price", "Quantity"],
                           aggfunc=[np.sum, np.mean], fill_value=0)
sales_report.head()

#Descriptive Statistics:
print(df[df["Product"]=="CPU"]["Quantity"].mean())
print(df[df["Product"]=="CPU"]["Price"].mean())
print(df[df["Product"]=="Software"]["Quantity"].mean())
print(df[df["Product"]=="Software"]["Price"].mean())

