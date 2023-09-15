import pandas as pd

path='C:\\Users\Didri\\Documents\\GitHub\\skole\\AI3000R\\train.csv'

data = pd.read_csv(path, nrows=10)

x = data.iloc[:, 0:20]
y = data.iloc[:, -1]

data_new = data.fillna(0)
data_new = data.fillna(data.median())

print("Data\n",data)

print("Data_new\n",data_new)