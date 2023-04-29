from django.urls import path
from django.conf.urls import *
from AppCoder.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('index/',login_required(index),name="index"),
    path('clientes/',login_required(clientes),name="clientes"),
    path('productos/',login_required(productos),name="productos"),
    path('stock/',login_required(stock),name="stock"),
    path('mostrar_codigos/',login_required(mostrar_codigos),name="mostrar_codigos"),
    path('mostrar_clientes/',login_required(mostrar_clientes),name="mostrar_clientes"),
    path('editar_codigos/<int:id_productos>',login_required(editar_codigos),name="editar_codigos"),
    path('editar_clientes/<int:id_clientes>',login_required(editar_clientes),name="editar_clientes"),
    path('eliminar_codigos/<int:id_productos>',login_required(eliminar_codigos),name="eliminar_codigos"),
    path('eliminar_clientes/<int:id_clientes>',login_required(eliminar_clientes),name="eliminar_clientes"),
    path('post/',login_required(post),name="post"),
    path('logout/',LogoutView.as_view(template_name="AppCoder/logout.html"),name="logout"),
    path('profile/',login_required(profile),name="profile"),
    path('profile/<str:username>/',login_required(profile),name="profile"),
    path('editarPerfil/',login_required(editarPerfil), name='editarPerfil'),
         
    ]

