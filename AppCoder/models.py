from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    correo=models.EmailField()

class productos(models.Model):
    codigo_producto=models.IntegerField()
    categoria_producto=models.CharField(max_length=20)

class stock(models.Model):
    codigo_producto=models.IntegerField()
    stock_nacional=models.IntegerField()
