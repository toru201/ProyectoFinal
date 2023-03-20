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

def guardar_forms(request):
    
    data={
         'form':ProductosForm()
    }
    if request.method == "POST":
        miFormulario = ProductosForm(data=request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
               
        else:
            data["form"] = miFormulario
 
    return render(request, 'AppCoder/guardar_forms.html', data)


def buscar_codigo(request):
    if request.method=="POST":
            print(f"\nEsta es la Informacion:{request.POST['codigo_producto']}\n")
            codigo= Productos.objects.filter(codigo=int(request.POST["codigo_producto"]))                   
            return render(request, "AppCoder/buscar_codigo.html",{"data":[codigo]})
    else:
            miFormulario = ProductosForm()
 
    return render(request, 'AppCoder/buscar_codigo.html', {"miFormulario": miFormulario})
