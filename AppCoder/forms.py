from django import forms
from AppCoder.models import Productos
from AppCoder.models import Clientes
from AppCoder.models import Stock

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
