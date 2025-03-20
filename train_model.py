import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Sample training data (replace with actual data if available)
X_train = np.array([
    [6.5, 4.2, 1.0, 500],  # Example input 1
    [7.0, 3.5, 0.8, 200],  # Example input 2
    [8.2, 2.1, 0.5, 50],   # Example input 3
    [5.5, 5.2, 1.2, 700]   # Example input 4
])
y_train = ["High Risk", "Low Risk", "Normal", "High Risk"]  # Corresponding labels

# Train the RandomForestClassifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
with open("prediction_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model trained and saved successfully!")
