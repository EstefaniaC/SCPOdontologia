# -*- coding:utf-8 -*-
from django import forms

from apps.cita.models import Cita
from apps.paciente.models import Paciente


class CitaForm(forms.ModelForm):

    class Meta:
        model = Cita
        fields = [
            'fecha',
            'hora',
            'paciente',
            'descripcion',
            'estado',
        ]
        labels = {
            'fecha': 'Fecha:',
            'hora': 'Hora:',
            'paciente': 'Paciente:',
            'descripcion': 'Descripción:',
            'estado': 'Estado de la cita:',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'js-datepicker form-control',
                                                                'data-date-format': 'yyyy-mm-dd'}),
            'hora': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(choices=Paciente.objects.all().filter(activo=True).values_list('id', 'nombre'),
                                     attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }