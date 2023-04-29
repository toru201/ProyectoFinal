from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request,'AppCoder/index.html')


def clientes(request):
    data={
         'form':ClientesForm()
    }
    if request.method == "POST":
        miFormulario = ClientesForm(data=request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
               
        else:
            data["form"] = miFormulario
 
    return render(request,'AppCoder/clientes.html',data)


def productos(request):
    data={
         'form':ProductosForm()
    }
    if request.method == "POST":
        miFormulario = ProductosForm(data=request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
               
        else:
            data["form"] = miFormulario
    return render(request,'AppCoder/productos.html',data)

def stock(request):
    data={
         'form':StockForm()
    }
    if request.method == "POST":
        miFormulario = StockForm(data=request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
               
        else:
            data["form"] = miFormulario
 
    return render(request,'AppCoder/stock.html',data)

def guardar_codigos(request):
    
    data={
         'form':ProductosForm()
    }
    if request.method == "POST":
        miFormulario = ProductosForm(data=request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
               
        else:
            data["form"] = miFormulario
 
    return render(request, 'AppCoder/guardar_codigos.html', data)

def mostrar_codigos(request):

    codigos=Productos.objects.all()

    return render(request, "AppCoder/mostrar_codigos.html",{"codigos":codigos})

def mostrar_clientes(request):

    
        codigos=Clientes.objects.all()
        return render(request, "AppCoder/mostrar_clientes.html",{"codigos":codigos})

def eliminar_codigos(request, id_productos):

    codigos=Productos.objects.get(id=id_productos)
    codigo_eliminado=codigos.codigo_producto
    codigos.delete()

    return render(request, "AppCoder/eliminar_codigos.html",{"codigo_eliminado":codigo_eliminado})

def eliminar_clientes(request, id_clientes):

    clientes=Clientes.objects.get(id=id_clientes)
    cliente_eliminado=clientes.correo
    clientes.delete()

    return render(request, "AppCoder/eliminar_clientes.html",{"cliente_eliminado":cliente_eliminado})

def editar_codigos(request, id_productos):
    
    codigos=Productos.objects.get(id=id_productos)

    if request.method=="POST":
        productos_form=ProductosForm(request.POST)
        if productos_form.is_valid():
            data=productos_form.cleaned_data
            codigos.codigo_producto=data["codigo_producto"]
            codigos.categoria_producto=data["categoria_producto"]
            codigos.save()
            return render(request, "AppCoder/index.html")
    else:
        productos_form=ProductosForm(initial={'codigo_producto':codigos.codigo_producto,'categoria_producto':codigos.categoria_producto})
        return render(request, "AppCoder/editar_codigos.html",{'form':productos_form})
    
def editar_clientes(request, id_clientes):
    
    clientes=Clientes.objects.get(id=id_clientes)

    if request.method=="POST":
        clientes_form=ClientesForm(request.POST)
        if clientes_form.is_valid():
            data=clientes_form.cleaned_data
            clientes.nombre=data["nombre"]
            clientes.apellido=data["apellido"]
            clientes.correo=data["correo"]
            clientes.save()
            return render(request, "AppCoder/index.html")
    else:
        clientes_form=ClientesForm(initial={'nombre':clientes.nombre,'apellido':clientes.apellido,'correo':clientes.correo})
        return render(request, "AppCoder/editar_clientes.html",{'form':clientes_form})

def buscar_codigo(request):
    if request.method=="POST":
            print(f"\nEsta es la Informacion:{request.POST['codigo_producto']}\n")
            codigo= Productos.objects.filter(codigo=int(request.POST["codigo_producto"]))                   
            return render(request, "AppCoder/buscar_codigo.html",{"data":[codigo]})
    else:
            miFormulario = ProductosForm()
 
    return render(request, 'AppCoder/buscar_codigo.html', {"miFormulario": miFormulario})




def post(request):
    current_user= get_object_or_404(User, pk=request.user.pk)
    if request.method=='POST':
        form= PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()
            messages.success(request,'Post enviado' )
            return render(request,'AppCoder/index.html')
    else:
        form=PostForm()
    return render(request, 'AppCoder/post.html', {'form': form})

def profile(request,username=None):
    current_user=request.user
    if username and username != current_user.username:
        user= User.objects.get(username=username)
        
    else:
        
        user=current_user
    return render(request, 'AppCoder/profile.html',{'user':user})

def editarPerfil(request):
       
      usuario = request.user
      
      if request.method == 'POST':
            
            miFormulario = UserEditForm(request.POST)
            
            if miFormulario.is_valid():
                
                  
                  informacion = miFormulario.cleaned_data
                  
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "AppCoder/index.html",{"mensaje": "Se edito exitosamente el usuario "})

      else:
            
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})