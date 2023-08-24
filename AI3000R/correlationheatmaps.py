import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path='C:\\Users\Didri\\Documents\\GitHub\\skole\\AI3000R\\train.csv'
data=pd.read_csv(path)

data_new = data.fillna(0)
data_new = data.fillna(data.median())

x=data_new.iloc[:, 0:20]
y=data_new.iloc[:, -1]

corrmat = data_new.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
g=sns.heatmap(data_new[top_corr_features].corr(),annot=True,cmap="RdYlGn")

plt.show()