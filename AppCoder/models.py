from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    correo=models.EmailField()

class Producto(models.Model):
    codigo_producto=models.IntegerField()
    categoria_producto=models.CharField(max_length=20)

class Stock(models.Model):
    codigo_producto=models.IntegerField()
    stock_nacional=models.IntegerField()
