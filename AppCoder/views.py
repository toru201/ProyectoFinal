from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'AppCoder/index.html')
def clientes(request):
    return render(request,'AppCoder/clientes.html')
def productos(request):
    return render(request,'AppCoder/productos.html')
def stock(request):
    return render(request,'AppCoder/stock.html')
