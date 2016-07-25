# -*- coding: utf-8 -*-
from django import forms
from apps.antecedentespersonales.models import AntecedentesPersonales
from apps.paciente.models import Paciente


class AntecedentesPersonalesForm(forms.ModelForm):

    class Meta:
        model = AntecedentesPersonales
        fields = [
            'paciente',
            'varicela',
            'rubeola',
            'sarampion',
            'parotiditis',
            'tosferina',
            'escarlatina',
            'parasitosis',
            'hepatitis',
            'sida',
            'asma',
            'endocrina',
            'hipertension',
            'cancer',
            'enfermedad_sexual',
            'epilepsia',
            'amigdalitis',
            'tuberculosis',
            'reumatica',
            'diabetes',
            'cardiovasculares',
            'artritis',
            'traumatismo',
            'quirurgicas',
            'sanguineas',
            'alergia',
        ]
        labels = {
            'paciente': 'Nombre del paciente:',
            'varicela': 'Varicela:',
            'rubeola': 'Rubéola:',
            'sarampion': 'Sarampión:',
            'parotiditis': 'Parotiditis:',
            'tosferina': 'Tosferina:',
            'escarlatina': 'Escarlatina:',
            'parasitosis': 'Parasitosis:',
            'hepatitis': 'Hepatitis:',
            'sida': 'Sida:',
            'asma': 'Asma:',
            'endocrina': 'Disfunsiones endocrinas',
            'hipertension': 'Hipertensión:',
            'cancer': 'Cáncer:',
            'enfermedad_sexual': 'Enfermedades de transmisión sexual:',
            'epilepsia': 'Epilepsia:',
            'amigdalitis': 'Amigdalitis de repetición:',
            'tuberculosis': 'Tuberculosis:',
            'reumatica': 'Reumatica:',
            'diabetes': 'Diabetes:',
            'cardiovasculares': 'Cardiovasculares:',
            'artritis': 'Artritis:',
            'traumatismo': 'Traumatismo',
            'quirurgicas': 'Intervenciones quirúrgicas:',
            'sanguineas': 'Transfunciones sanguineas:',
            'alergia': 'Alergías a:',
        }
        widgets = {
            'paciente':forms.Select(choices=Paciente.objects.all().filter(activo=True).values_list('id','nombre'),
                                    attrs={'class':'form-control'}),
            'alergia': forms.TextInput(attrs={'class':'form-control'}),
         }