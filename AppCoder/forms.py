from django import forms
from AppCoder.models import productos
from AppCoder.models import clientes
from AppCoder.models import stock

class ProductosForm(forms.ModelForm):
    class Meta:
        model=productos
        fields=[
            "codigo_producto",
            "categoria_producto"
        ]
        labels={
            'codigo_producto': "codigo",
            'categoria_producto':'categoria'}
        widget={
            'codigo_producto': forms.TextInput(attrs={'class':'form-control'}),
            'categoria_producto':forms.TextInput(attrs={'class':'form-control'}),
        }

class ClientesForm(forms.ModelForm):
    class Meta:
        model=clientes
        fields='__all__'

class StockForm(forms.ModelForm):
    class Meta:
        model=stock
        fields='__all__'

class BuscarCodigoForm(forms.ModelForm):
    codigo=forms.CharField(max_length=20)
