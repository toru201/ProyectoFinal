from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('index/',index,name="index"),
    path('clientes/',clientes,name="clientes"),
    path('productos/',productos,name="productos"),
    path('stock/',stock,name="stock"),
    path('mostrar_codigos/',mostrar_codigos,name="mostrar_codigos"),
    #path('guardar_codigos/',guardar_codigos,name="guarda_formulario"),#no se usa#
    path('editar_codigos/<int:id_productos>',editar_codigos,name="editar_codigos"),
    path('eliminar_codigos/<int:id_productos>',eliminar_codigos,name="eliminar_codigos"),
    #path('buscar_codigo/',buscar_codigo,name="busca_codigo") 
    ]