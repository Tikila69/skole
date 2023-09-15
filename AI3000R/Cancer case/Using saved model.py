import numpy as np
import joblib

path = "C:\\Users\Didri\\Documents\\GitHub\\skole\\AI3000R\\Cancer case\\cancer_prediction_model.joblib"

# Load the saved model
model_filename = path
loaded_model = joblib.load(model_filename)

# Example new data (replace this with your actual data)
new_data = np.array([[1000025,5,1,1,1,2,1,3,1,1]])

# Make predictions using the loaded model
prediction = loaded_model.predict(new_data)

# Interpret the prediction
if prediction[0] == 2:
    print("Predicted: Benign")
else:
    print("Predicted: Malignant")
