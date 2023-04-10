from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('index/',index,name="index"),
    path('clientes/',clientes,name="clientes"),
    path('productos/',productos,name="productos"),
    path('stock/',stock,name="stock"),
    path('mostrar_codigos/',mostrar_codigos,name="mostrar_codigos"),
    path('mostrar_clientes/',mostrar_clientes,name="mostrar_clientes"),
    path('editar_codigos/<int:id_productos>',editar_codigos,name="editar_codigos"),
    path('editar_clientes/<int:id_clientes>',editar_clientes,name="editar_clientes"),
    path('eliminar_codigos/<int:id_productos>',eliminar_codigos,name="eliminar_codigos"),
    path('eliminar_clientes/<int:id_clientes>',eliminar_clientes,name="eliminar_clientes"),
    path('post/',post,name="post"),
    path('register/',register,name="register"),
    path('login/',LoginView.as_view(template_name="AppCoder/login.html"),name="login"),
    path('logout/',LogoutView.as_view(template_name="AppCoder/logout.html"),name="logout"),
         
    ]

