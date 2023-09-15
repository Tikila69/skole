from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

path = "C:\\Users\Didri\\Documents\\GitHub\\skole\\AI3000R\\FB Competition.csv"

data = pd.read_csv(path)

time_value = pd.to_datetime(data['time'], unit='s')
data["day"] = time_value.dt.day
data["weekday"] = time_value.dt.weekday
data["hour"] = time_value.dt.hour

x = data[["x", "y", "accuracy", "day", "weekday", "hour"]]
y = data["place_id"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)  # Corrected this line

k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(x_train_scaled, y_train)

y_pred = knn.predict(x_test_scaled)  # Corrected this line
print("Accuracy: ", accuracy_score(y_test, y_pred))
