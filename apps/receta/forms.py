# -*- coding: utf-8 -*-
from django import forms
from apps.receta.models import Receta
from apps.paciente.models import Paciente


class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = [
            'paciente',
            'fecha',
            'receta',
        ]
        labels = {
            'paciente': 'Nombre del paciente:',
            'fecha': 'Fecha:',
            'receta': 'Receta:',
        }
        widgets = {
            'paciente':forms.Select(choices=Paciente.objects.all().filter(activo=True).values_list('id','nombre'),
                                    attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'js-datepicker form-control',
                                            'data-date-format': 'yyyy-mm-dd'}),
            'receta': forms.Textarea(attrs={'class': 'form-control'}),
         }