from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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

def feed(request):
    posts= Post.objects.all()
    context={'post':posts}
    return render(request, 'AppCoder/feed.html',context)

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else:
        form=UserRegisterForm()
    context={'form':form}
    return render(request, 'AppCoder/register.html', context)