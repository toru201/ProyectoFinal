from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.
def index(request):
    return render(request,'AppCoder/index.html')
def clientes(request):
    return render(request,'AppCoder/clientes.html')
def productos(request):
    return render(request,'AppCoder/productos.html')
def stock(request):
    return render(request,'AppCoder/stock.html')

def guardar_forms(request):
 
    if request.method == "POST":
        miFormulario = ProductosForm(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
        return render(request, "AppCoder/index.html")
    
    else:
      
      miFormulario = ProductosForm()
 
    return render(request, 'AppCoder/guardar_forms.html', {"miFormulario": miFormulario})


def buscar_codigo(request):
    if request.method == "POST":
            print(f"\nEsta es la Informacion:{request.POST['codigo']}\n")
            codigo= ProductosForm.objects.filter(codigo=int(request.POST["codigo"]))
                         
            return render(request, "AppCoder/buscar_codigo.html",{"data":[codigo]})
    else:
            miFormulario = ProductosForm()
 
    return render(request, 'AppCoder/buscar_codigo.html', {"miFormulario": miFormulario})
