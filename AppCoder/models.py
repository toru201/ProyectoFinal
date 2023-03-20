from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    correo=models.EmailField()

class Productos(models.Model):
    codigo_producto=models.IntegerField()
    categoria_producto=models.CharField(max_length=20)

class Stock(models.Model):
    codigo_producto=models.IntegerField()
    stock_nacional=models.IntegerField()
