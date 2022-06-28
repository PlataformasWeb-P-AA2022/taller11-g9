from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, Departamento

# Form Edificio
class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese el nombre del Edificio por favor'),
            'direccion': _('Ingrese la direccion por favor'),
            'ciudad': _('Ingrese la ciudad por favor'),
            'tipo': _('Ingrese el tipo de Edificio por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())

        if num_palabras < 1:
            raise forms.ValidationError("Ingrese el nombre del Edificio por favor")
        return valor

    def clean_direccion(self):
        valor = self.cleaned_data['direccion']
        num_palabras = len(valor.split())

        if num_palabras < 1:
            raise forms.ValidationError("Ingrese la direccion por favor")
        return valor

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        num_palabras = len(valor.split())
        
        if num_palabras < 1:
            raise forms.ValidationError("Ingrese la ciudad por favor")

    def clean_tipo(self):       
        valor = self.cleaned_data['tipo']
        num_palabras = len(valor.split())
        
        if num_palabras < 1:
            raise forms.ValidationError("Ingrese el tipo de Edificio por favor")
        return valor
     
# Form Departamento   
class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'numCuartos', 'edificio']
