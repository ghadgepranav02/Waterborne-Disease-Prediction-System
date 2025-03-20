from django import forms

class PredictionForm(forms.Form):
    ph_level = forms.FloatField(label="pH Level")
    turbidity = forms.FloatField(label="Turbidity")
    chlorine_level = forms.FloatField(label="Chlorine Level")
    bacteria_count = forms.IntegerField(label="Bacteria Count")
