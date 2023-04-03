from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *


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

def eliminar_codigos(request, id_productos):

    codigos=Productos.objects.get(id=id_productos)
    codigo_eliminado=codigos.codigo_producto
    codigos.delete()

    return render(request, "AppCoder/eliminar_codigos.html",{"codigo_eliminado":codigo_eliminado})

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

def buscar_codigo(request):
    if request.method=="POST":
            print(f"\nEsta es la Informacion:{request.POST['codigo_producto']}\n")
            codigo= Productos.objects.filter(codigo=int(request.POST["codigo_producto"]))                   
            return render(request, "AppCoder/buscar_codigo.html",{"data":[codigo]})
    else:
            miFormulario = ProductosForm()
 
    return render(request, 'AppCoder/buscar_codigo.html', {"miFormulario": miFormulario})
