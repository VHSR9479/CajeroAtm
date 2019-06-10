from django import forms

# Modelo para Banco
class Banco(forms.Form):
    id_banco  = forms.IntegerField(primary_key=True, unique=True, editable=False)
    nit       = forms.CharField(max_length=10)
    nombre    = forms.CharField(max_length=45)
    direccion = forms.CharField(max_length=45)
    telefono  = forms.CharField(max_length=10)
