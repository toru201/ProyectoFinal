from django.urls import path
from AppCoder.views import *
from AppCoder.views import buscar_codigo

urlpatterns = [
    path('index/',index,name="index"),
    path('clientes/',clientes,name="clientes"),
    path('productos/',productos,name="productos"),
    path('stock/',stock,name="stock"),
    path('guardar_forms/',guardar_forms,name="guarda_formulario"),
    path('buscar_codigo/',buscar_codigo,name="busca_codigo")
    ]