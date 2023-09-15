import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree


path = 'C:\\Users\Didri\\Documents\\GitHub\\skole\\AI3000R\\Titanic.csv'

data = pd.read_csv(path)

data["Sex"] = data["Sex"].map({"female":0,"male":1})

data["Age"] = data["Age"].fillna(data["Age"].median())

x = data[["Pclass", "Age", "Sex"]]
y = data["Survived"]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=22)

classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy: ", accuracy.round(2))

plt.figure(figsize=(12, 8))
plot_tree(classifier, feature_names=["Pclass","Age","Sex"], filled=True, class_names=["Dead", "Survived"])
plt.show()

newData = pd.DataFrame([[1, 50, 0]],columns=["Pclass", "Age", "Sex"])
prediction = classifier.predict(newData)
predictionMapped = ["Survived" if prediction[0] == 1 else "Dead" for pred in prediction]

print("Prediction: ", predictionMapped)