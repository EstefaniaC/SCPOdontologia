# -*- coding:utf-8 -*-
from django import forms

from apps.antecedentesfamiliares.models import AntecedentesFamiliares
from apps.paciente.models import Paciente

class AntecedentesFamiliaresForm(forms.ModelForm):

    class Meta:
        model = AntecedentesFamiliares
        fields = [
            'paciente',
            'diabetes',
            'hipertension',
            'cardiopatia',
            'neoplasia',
            'epilepsia',
            'malformacion',
            'sida',
            'renales',
            'epatitis',
            'artritis',
            'sano',
        ]
        labels = {       
            'paciente': 'Nombre del Paciente:',
            'diabetes': 'Diabetes:',
            'hipertension': 'hipertensión arterial:',
            'cardiopatia': 'Cardiopatias:',
            'cardiopatia': 'Cardiopatias:',
            'neoplasia': 'Neoplasia:',
            'epilepsia': 'Epilepsia:',
            'malformacion': 'Malformaciones:',
            'sida': 'SIDA:',
            'renales': 'Enfermedades renales:',
            'epatitis': 'Epatitis:',
            'artritis': 'Artritis:',
            'sano': 'Aperentemente sano:',
        }
        widgets = {
           
            'paciente': forms.Select(choices=Paciente.objects.all().filter(activo=True).values_list('id','nombre'),
                                    attrs={'class': 'form-control'}),
            'diabetes': forms.TextInput(attrs={'class': 'form-control'}),
            'hipertension': forms.TextInput(attrs={'class': 'form-control'}),
            'cardiopatia': forms.TextInput(attrs={'class': 'form-control'}),
            'neoplasia': forms.TextInput(attrs={'class': 'form-control'}),
            'epilepsia': forms.TextInput(attrs={'class': 'form-control'}),
            'malformacion': forms.TextInput(attrs={'class': 'form-control'}),
            'sida': forms.TextInput(attrs={'class': 'form-control'}),
            'renales': forms.TextInput(attrs={'class': 'form-control'}),
            'epatitis': forms.TextInput(attrs={'class': 'form-control'}),
            'artritis': forms.TextInput(attrs={'class': 'form-control'}),
            'sano': forms.TextInput(attrs={'class': 'form-control'}),
        }