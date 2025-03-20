from django.urls import path
from .views import home, predict_disease  # ✅ Import `home`

urlpatterns = [
    path("", home, name="home"),  # ✅ Add home route
    path("predict/", predict_disease, name="predict_disease"),
]
