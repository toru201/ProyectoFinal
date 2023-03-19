from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('',index,name="index"),
    path('clientes/',clientes,name="clientes"),
    path('productos/',productos,name="productos"),
    path('stock/',stock,name="stock"),
    ]