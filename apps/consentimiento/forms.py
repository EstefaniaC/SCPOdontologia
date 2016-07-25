# -*- coding:utf-8 -*-
from django import forms

from apps.consentimiento.models import Consentimiento
from apps.paciente.models import Paciente
from apps.interconsulta.models import Interconsulta


class ConsentimientoForm(forms.ModelForm):

    class Meta:
        model = Consentimiento
        fields = [
            'paciente',
            'interconsulta',
        ]
        labels = {
            'paciente': 'Nombre del paciente:',
            'interconsulta': 'Persona responsable del paciente:',
        }
        widgets = {
            'paciente': forms.Select(choices=Paciente.objects.all().filter(activo=True).values_list('id', 'nombre'),
                                     attrs={'class': 'form-control'}),
            'interconsulta': forms.Select(choices=Interconsulta.objects.all().filter(activo=True).values_list('id', 'persona_responsable'),
                                     attrs={'class': 'form-control'}),
        }