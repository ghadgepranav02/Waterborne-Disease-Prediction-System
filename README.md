# 💧 Waterborne Disease Prediction System

A Django-based web application that predicts the risk level of waterborne diseases using a machine learning model (Random Forest Classifier). The system analyzes water quality parameters and classifies the risk as **High Risk**, **Low Risk**, or **Normal**.

---

## 🚀 Features

- Water quality risk prediction using a trained ML model
- Django web interface for submitting water parameters
- Pre-trained `RandomForestClassifier` model served via pickle
- Static file support for a polished frontend
- SQLite database for lightweight data storage

---

## 🧠 ML Model

The prediction model (`prediction_model.pkl`) is trained on water quality parameters:

| Feature | Description |
|---|---|
| pH Level | Acidity/alkalinity of water |
| Turbidity | Cloudiness of water |
| Contamination Index | Measured contamination level |
| Bacteria Count | Number of bacteria per mL |

**Output labels:**
- `High Risk` — Water is unsafe, immediate action needed
- `Low Risk` — Minor concerns, monitoring recommended
- `Normal` — Water quality is within safe limits

To retrain the model:
```bash
python train_model.py
```

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **ML:** scikit-learn (RandomForestClassifier), NumPy
- **Database:** SQLite
- **Frontend:** HTML/CSS (Django templates)

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/waterborne-disease-prediction.git
cd waterborne-disease-prediction
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure

```
waterborne-disease-prediction/
├── waterborne_disease/       # Django project settings & URLs
├── prediction/               # Django app — views, models, forms
├── templates/                # HTML templates
├── static/                   # CSS, JS, images
├── staticfiles/              # Collected static files (for deployment)
├── train_model.py            # Script to train the ML model
├── prediction_model.pkl      # Pre-trained RandomForest model
├── manage.py                 # Django management utility
├── db.sqlite3                # SQLite database
└── requirements.txt          # Python dependencies
```

---

## 📦 Requirements

Make sure `requirements.txt` includes:

```
django
scikit-learn
numpy
```

Generate it with:
```bash
pip freeze > requirements.txt
```

---

## 🧪 Retraining the Model

Edit `train_model.py` with your actual dataset, then run:
```bash
python train_model.py
```

This saves a new `prediction_model.pkl` that the Django app will automatically use.

---

## 🌐 Deployment Notes

- Run `python manage.py collectstatic` before deploying to collect all static files into `staticfiles/`
- Set `DEBUG = False` in `waterborne_disease/settings.py` for production
- Use a production-grade database (PostgreSQL recommended) instead of SQLite for live deployments

---


**Your Name**  
[GitHub](https://github.com/your-username) • [LinkedIn](https://linkedin.com/in/your-profile)
