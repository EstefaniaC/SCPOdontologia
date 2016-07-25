# -*- coding: utf-8 -*-
from django import forms
from apps.paciente.models import Paciente
from apps.tratamiento.models import Tratamiento


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'edad',
            'lugar_nacimiento',
            'fecha_nacimiento',
            'telefono',
            'celular',
            'correo_electronico',
            'direccion',
            'recomendado',
            'observaciones',
            'motivo_consulta',
            'dolor',
            'control',
            'sangrado_encia',
            'restauracion_protesica',
            'enfermedad_actual',
            'tratamiento',            
            'ocupacion',
        ]
        labels = {
            'nombre': 'Nombre:',
            'apellido_paterno': 'Apellido Paterno:',
            'apellido_materno': 'Apellido Materno:',
            'edad': 'Edad:',
            'lugar_nacimiento': 'Lugar de Nacimiento:',
            'fecha_nacimiento': 'Fecha de Nacimiento:',
            'telefono': 'Teléfono:',
            'celular': 'Celular:',
            'correo_electronico': 'Correo electrónico',
            'direccion': 'Dirección:',
            'recomendado': 'Quién lo recomendó:',
            'observaciones': 'Observaciones:',
            'motivo_consulta': 'Motivo de la consulta:',
            'dolor': 'Dolor:',
            'control': 'Control:',
            'sangrado_encia': 'Sangrado en las encías:',
            'restauracion_protesica': 'Restauración protésica:',
            'enfermedad_actual': 'Enfermedad actual:',
            'tratamiento': 'Tratamiento:',
            'ocupacion': 'Ocupación:',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'lugar_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'js-datepicker form-control',
                                                                'data-date-format': 'yyyy-mm-dd'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'recomendado': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'motivo_consulta': forms.TextInput(attrs={'class': 'form-control'}),
            'dolor': forms.TextInput(attrs={'class': 'form-control'}),
            'control': forms.TextInput(attrs={'class': 'form-control'}),
            'sangrado_encia': forms.TextInput(attrs={'class': 'form-control'}),
            'restauracion_protesica': forms.TextInput(attrs={'class': 'form-control'}),
            'enfermedad_actual': forms.TextInput(attrs={'class': 'form-control'}),
            'tratamiento': forms.Select(choices=Tratamiento.objects.all().filter(activo=True).values_list('id', 'nombre'),
                                    attrs={'class': 'form-control'}),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control'}),
        }