import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    # Sample dataset (replace with real data later)
    data = {
        'ph': [7.0, 6.5, 8.1, 5.5, 7.2, 6.8, 4.5, 9.0],
        'turbidity': [2.0, 4.5, 1.0, 6.0, 2.5, 3.2, 8.0, 1.2],
        'chlorine_level': [0.5, 1.0, 0.3, 1.5, 0.7, 0.9, 0.1, 1.2],
        'bacteria_count': [10, 50, 5, 100, 20, 30, 200, 2],
        'disease_risk': [1, 1, 0, 1, 0, 0, 1, 0]  # 1 = High risk, 0 = Low risk
    }

    df = pd.DataFrame(data)

    # Splitting data
    X = df[['ph', 'turbidity', 'chlorine_level', 'bacteria_count']]
    y = df['disease_risk']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, 'prediction_model.pkl')

    print("Model trained and saved successfully!")

# Train the model when this script is run
if __name__ == "__main__":
    train_model()
