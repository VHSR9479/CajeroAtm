from django import forms
from Atm.models import Banco
# Modelo para Banco
class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco

        fields = [
            "id_banco",
            "nit",
            "nombre",
            "direccion",
            "telefono",
        ]

        labels = {
            "id_banco" : 'Identificacion Banco',
            "nit": "Nit Banco",
            "nombre" : "Nombre Banco",
            "direccion": "Direccion Banco",
            "telefono" : "Telefono Banco",
        }

        widgets = {
            "id_banco": forms.TextInput(attrs = {'class':'form-control'}),
            "nit": forms.TextInput(attrs = {'class':'form-control'}),
            "nombre": forms.TextInput(attrs = {'class':'form-control'}),
            "direccion": forms.TextInput(attrs = {'class':'form-control'}),
            "telefono": forms.TextInput(attrs = {'class':'form-control'}),
        }
