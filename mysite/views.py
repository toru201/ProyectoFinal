from django.http import HttpResponse
from django.template import Template
from django.template import Context
from django.template import loader

def saludo (request):
	return HttpResponse("Hola Django - Coder")
def saludo_2 (request):
	return HttpResponse("Hola Django - Coder2")

def probandoTemplate(request):
	# mihtml=open("./templates/template1.html")
	# plantilla = Template(mihtml.read())
	# mihtml.close()
    plantilla=loader.get_template("template1.html")
	# mi_contexto= Context()
    documento = plantilla.render()
    return HttpResponse(documento)

def index(request):
	diccionario={"nombre": "Coder"}
	plantilla=loader.get_template("index.html")
	documento=plantilla.render(diccionario)
	return HttpResponse(documento)