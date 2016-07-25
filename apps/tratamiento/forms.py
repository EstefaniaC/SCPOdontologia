# -*- coding: utf-8 -*-
from django import forms
from apps.tratamiento.models import Tratamiento


class TratamientoForm(forms.ModelForm):

    class Meta:
        model = Tratamiento
        fields = [
            'nombre',
            'descripcion',
            'precio',
        ]
        labels = {
            'nombre': 'Nombre:',
            'descripcion': 'Descripción:',
            'precio': 'Precio:',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
        }
