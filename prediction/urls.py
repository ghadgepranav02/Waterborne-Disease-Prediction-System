from django.urls import path
from .views import home, predict_disease, download_pdf
from . import views




urlpatterns = [
    path("", home, name="home"),                 # optional
    path("predict/", predict_disease, name="predict_disease"),
    path("download/", download_pdf,   name="download_pdf"),
]
from django.urls import path, include
