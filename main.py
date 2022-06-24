import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/muruganusha/PyCharm/googleplaystore.csv')

a1=df.head()
a2=df.describe()
a3=df.shape
a4=df.info()

print(a4)

a=df.isnull().sum()
print(a)






