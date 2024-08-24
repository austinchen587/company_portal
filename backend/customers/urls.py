from django.urls import path
from .views import upload_file, customer_analysis

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('analysis/', customer_analysis, name='customer_analysis'),
]