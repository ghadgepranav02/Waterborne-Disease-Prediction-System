from django.shortcuts import render
import os
import pickle
import numpy as np
from django.conf import settings
from .forms import PredictionForm

# ✅ Correct Model Path
MODEL_PATH = os.path.join(settings.BASE_DIR, "prediction_model.pkl")

# ✅ Check if model exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"🚨 Model file not found at: {MODEL_PATH}")

# ✅ Load the trained model
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# ✅ Ensure the model has a predict method
if not hasattr(model, "predict"):
    raise TypeError("🚨 Model does not have a 'predict' method! Train it properly.")

# ✅ Home Page Function (Fixes the error)
def home(request):
    return render(request, "prediction/home.html")

# ✅ Prediction Function
def predict_disease(request):
    prediction = None
    explanation = ""
    report_details = None

    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Get user input
            ph_level = form.cleaned_data["ph_level"]
            turbidity = form.cleaned_data["turbidity"]
            chlorine_level = form.cleaned_data["chlorine_level"]
            bacteria_count = form.cleaned_data["bacteria_count"]

            # Convert input into model format
            input_data = np.array([[ph_level, turbidity, chlorine_level, bacteria_count]])

            # Make prediction
            risk_level = model.predict(input_data)[0]

            # Assign detailed explanation
            explanation_dict = {
                "High Risk": "⚠️ The water is highly contaminated and unsafe for consumption.",
                "Normal": "✅ Water quality is within safe limits.",
                "Low Risk": "⚠️ Water shows slight contamination. Consider purification."
            }
            explanation = explanation_dict.get(risk_level, "Unknown risk level.")

            prediction = risk_level

            # ✅ Generate a Detailed Report
            report_details = f"""
            <h4>📝 Water Quality Report</h4>
            <ul>
                <li><strong>pH Level:</strong> {ph_level} (Safe range: 6.5 - 8.5)</li>
                <li><strong>Turbidity:</strong> {turbidity} NTU (Safe range: 0 - 5 NTU)</li>
                <li><strong>Chlorine Level:</strong> {chlorine_level} mg/L (Safe range: 0.2 - 1.0 mg/L)</li>
                <li><strong>Bacteria Count:</strong> {bacteria_count} CFU/mL (Safe range: < 500 CFU/mL)</li>
            </ul>
            <p><strong>Risk Assessment:</strong> {prediction}</p>
            <p>{explanation}</p>
            """

    else:
        form = PredictionForm()

    return render(request, "prediction/predict.html", {
        "form": form, 
        "prediction": prediction, 
        "explanation": explanation, 
        "report": report_details
    })
