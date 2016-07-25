# -*- coding: utf-8 -*-
from django import forms
from apps.interconsulta.models import Interconsulta
from apps.paciente.models import Paciente
from apps.tratamiento.models import Tratamiento


class InterconsultaForm(forms.ModelForm):

    class Meta:
        model = Interconsulta
        fields = [
            'paciente',
            'persona_responsable',
            'parentesco',
            'diagnostico',
            'complicaciones',
            'motivo',
            'servicio',
            'resumen_clinico',
            'estudio',
            'criterio',
            'tratamiento',
        ]
        labels = {
            'paciente': 'Nombre del paciente:',
            'persona_responsable': 'Persona responsable del paciente:',
            'parentesco': 'Parentesco:',
            'diagnostico': 'Diagnóstico:',
            'complicaciones': 'Complicaciones:',
            'motivo': 'Motivo:',
            'servicio': 'Servicio ó Especialidad:',
            'resumen_clinico': 'Resumen clínico:',
            'estudio': 'Estudios de laboratorios y/ó  Gabinete:',
            'criterio': 'Sugerencias, Diagnóstico y Criterios:',
            'tratamiento': 'Tratamiento:',
        }
        widgets = {
            'paciente': forms.Select(choices=Paciente.objects.all().filter(activo=True).values_list('id'),
                                    attrs={'class':'form-control'}),
            'persona_responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'parentesco': forms.TextInput(attrs={'class':'form-control'}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control'}),
            'complicaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control'}),
            'servicio': forms.Textarea(attrs={'class': 'form-control'}),
            'resumen_clinico': forms.Textarea(attrs={'class': 'form-control'}),
            'estudio': forms.Textarea(attrs={'class': 'form-control'}),
            'criterio': forms.Textarea(attrs={'class': 'form-control'}),
            'tratamiento': forms.Select(choices=Tratamiento.objects.all().filter(activo=True).values_list('id', 'nombre'),
                                        attrs={'class':'form-control'}),
         }