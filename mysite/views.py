from django.http import HttpResponse
from django.template import Template
from django.template import Context
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

def inicio(request):
	diccionario={"nombre": "Coder"}
	plantilla=loader.get_template("inicio.html")
	documento=plantilla.render(diccionario)
	return HttpResponse(documento)

def about(request):
      return render(request, "about.html") 

class VRegistro(View):
	def get (self,request):
		form=UserCreationForm()
		return render (request,"register.html",{"form":form})
	   
	def post(self,request):
			form=UserCreationForm(request.POST)

			if form.is_valid():
				usuario=form.save()
				login(request, usuario)
				return render(request, "AppCoder/index.html")
			
			else:
				for msg in form.error_messages:
					messages.error(request,form.error_messages[msg])
				return render (request,"register.html",{"form":form})

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppCoder/index.html")
            else:
                messages.error(request,"usuario no valido")
        else:
            messages.error(request,"informacion incorrecta")

    form=AuthenticationForm()
    return render(request,"logear.html",{"form":form})
