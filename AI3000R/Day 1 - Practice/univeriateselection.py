import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

path='C:\\Users\Didri\\Documents\\GitHub\\skole\\AI3000R\\train.csv'
data=pd.read_csv(path)

data_new = data.fillna(0)
data_new = data.fillna(data.median())

x=data_new.iloc[:, 0:20]
y=data_new.iloc[:, -1]

bestfeatures = SelectKBest(score_func=chi2, k=5)
fit = bestfeatures.fit(x,y)
dfscores = pd.DataFrame(fit.scores_)

dfcolumns = pd.DataFrame(x.columns)
scores = pd.concat([dfcolumns,dfscores],axis=1)
scores.columns = ['Specs','Score']
print(scores.nlargest(5,'Score'))