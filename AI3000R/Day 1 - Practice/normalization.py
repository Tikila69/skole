from sklearn.preprocessing import MinMaxScaler
import pandas as pd

path='C:\\Users\Didri\\Documents\\GitHub\\skole\\AI3000R\\Scaling-dating.txt'
data=pd.read_csv(path,delimiter="\t")
data=data.iloc[:,:3]
transfer = MinMaxScaler(feature_range=(1, 2))
data_new = transfer.fit_transform(data)
print(data_new)