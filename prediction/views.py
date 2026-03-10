import os
import pickle
import numpy as np
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import PredictionForm

# ————————————————————————————————
# 1) Load your model once at import time
MODEL_PATH = os.path.join(settings.BASE_DIR, "prediction_model.pkl")
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

if not hasattr(model, "predict"):
    raise TypeError("Loaded model has no .predict() method")

# ————————————————————————————————
# 2) Home view (if you need one)
def home(request):
    return render(request, "prediction/home.html")

# ————————————————————————————————
# 3) Prediction view
def predict_disease(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            ph      = form.cleaned_data["ph_level"]
            turb    = form.cleaned_data["turbidity"]
            chl     = form.cleaned_data["chlorine_level"]
            bact    = form.cleaned_data["bacteria_count"]

            X = np.array([[ph, turb, chl, bact]])
            risk = model.predict(X)[0]

            explanations = {
                "High Risk": "⚠️ The water is highly contaminated and unsafe for consumption.",
                "Normal":    "✅ Water quality is within safe limits.",
                "Low Risk":  "⚠️ Water shows slight contamination. Consider purification."
            }
            explanation = explanations.get(risk, "Unknown risk level.")

            # store for PDF
            request.session["ph_level"]      = ph
            request.session["turbidity"]     = turb
            request.session["chlorine_level"]= chl
            request.session["bacteria_count"]= bact
            request.session["prediction"]    = risk
            request.session["explanation"]   = explanation

            # render results page
            return render(request, "prediction/results.html", {
                "ph_level":       ph,
                "turbidity":      turb,
                "chlorine_level": chl,
                "bacteria_count": bact,
                "prediction":     risk,
                "explanation":    explanation,
                # optional: bootstrap alert class
                "alert_class":    {
                    "High Risk": "danger",
                    "Normal":    "success",
                    "Low Risk":  "warning"
                }.get(risk, "info")
            })
    else:
        form = PredictionForm()

    # GET or invalid POST
    return render(request, "prediction/predict.html", {"form": form})

# ————————————————————————————————
# 4) PDF download view (unchanged)
def download_pdf(request):
    template_path = 'prediction/pdf_template.html'
    context = {
        'ph_level':       request.session.get('ph_level',      'N/A'),
        'turbidity':      request.session.get('turbidity',     'N/A'),
        'chlorine_level': request.session.get('chlorine_level','N/A'),
        'bacteria_count': request.session.get('bacteria_count','N/A'),
        'prediction':     request.session.get('prediction',    'N/A'),
        'explanation':    request.session.get('explanation',   'N/A'),
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="water_quality_report.pdf"'

    template = get_template(template_path)
    html     = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF generation failed.')
    return response
