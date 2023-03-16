from django.urls import path
from AppCoder.views import inicio, index

urlpatterns = [
    path('', inicio),
    path('index/',index)
    ]