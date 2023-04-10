from django import forms
from AppCoder.models import Productos
from AppCoder.models import Clientes
from AppCoder.models import Stock
from AppCoder.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductosForm(forms.ModelForm):
    class Meta:
        model=Productos
        fields=[
        "codigo_producto",
        "categoria_producto"
        ]
        labels={
            'codigo_producto': "Codigo",
            'categoria_producto':'Categoria'}
        widget={
            'codigo_producto': forms.TextInput(attrs={'class':'form-control'}),
            
            'categoria_producto':forms.TextInput(attrs={'class':'form-control'}),
        }

class ClientesForm(forms.ModelForm):
    class Meta:
        model=Clientes
        fields='__all__'

class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields='__all__'

class BuscarCodigoForm(forms.Form):
    codigo=forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        help_texts={k:"" for k in fields}

class PostForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100',
                                'id':'contentsBox','rows':'3',
                                'placeholder':'Qué hiciste durante la sesión?'}))

    class Meta:
        model= Post
        fields= ['content']

class UserEditForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}
    
    
       
                                                                   