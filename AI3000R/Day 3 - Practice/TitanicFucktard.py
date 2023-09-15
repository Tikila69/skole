import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler

path = "C:\\Users\Didri\\Documents\\GitHub\\skole\\AI3000R\\Titanic.csv"

# Load the Titanic dataset
df = pd.read_csv(path, delimiter=',')

print(df.columns)

# Print column names to debug
print("Column names:", df.columns)

# Drop rows where 'Pclass', 'Sex', or 'Age' is NaN
df.dropna(subset=['Pclass', 'Sex', 'Age'], inplace=True)

# Convert 'Sex' to numerical values
label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])

# Create feature matrix and target vector
X = df[['Pclass', 'Sex', 'Age']].values
y = df['Survived'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create a Decision Tree Classifier
clf = DecisionTreeClassifier(max_depth=4, random_state=42)

# Fit the classifier to the training data
clf.fit(X_train, y_train)
print("Feature importances:", clf.feature_importances_)
# Predict on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Plot the decision tree
feature_names = ['Pclass', 'Sex', 'Age']
class_names = ['Not Survived', 'Survived']
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=feature_names, class_names=class_names, filled=True)
new_data = pd.DataFrame([[50,1,1]], columns=["Age", "Pclass", "Sex"])
prediction = clf.predict(new_data)
prediction_mapped = ["survived" if pred == 1 else "not survived" for pred in prediction]
print("Prediction:", prediction_mapped)
plt.show()