from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    correo=models.EmailField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido} - {self.correo} "

class Productos(models.Model):
    codigo_producto=models.IntegerField()
    categoria_producto=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.id} - {self.codigo_producto} - {self.categoria_producto}"

class Stock(models.Model):
    codigo_producto=models.IntegerField()
    stock_nacional=models.IntegerField()
    def __str__(self):
        return f"{self.id} - {self.codigo_producto} - {self.stock_nacional}"
    
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    timestamp=models.DateTimeField(default=timezone.now)
    content=models.TextField()

    class Meta:
        ordering=['-timestamp']
    
    def __str__(self):
        return f'{self.user.username}: {self.content}'

def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


