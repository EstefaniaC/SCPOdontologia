from django.db import models

from apps.paciente.models import Paciente

# Create your models here.

class AntecedentesPersonales(models.Model):
    
    paciente = models.ForeignKey(Paciente, null=True, blank=True)
    varicela = models.BooleanField(default=True)
    rubeola = models.BooleanField(default=True)
    sarampion = models.BooleanField(default=True)
    parotiditis = models.BooleanField(default=True)
    tosferina = models.BooleanField(default=True)
    escarlatina = models.BooleanField(default=True)
    parasitosis = models.BooleanField(default=True)
    hepatitis = models.BooleanField(default=True)
    sida = models.BooleanField(default=True)
    asma = models.BooleanField(default=True)
    endocrina = models.BooleanField(default=True)
    hipertension = models.BooleanField(default=True)
    cancer = models.BooleanField(default=True)
    enfermedad_sexual = models.BooleanField(default=True)
    epilepsia = models.BooleanField(default=True)
    amigdalitis = models.BooleanField(default=True)
    tuberculosis = models.BooleanField(default=True)
    reumatica = models.BooleanField(default=True)
    diabetes = models.BooleanField(default=True)
    cardiovasculares = models.BooleanField(default=True)
    artritis = models.BooleanField(default=True)
    traumatismo = models.BooleanField(default=True)
    quirurgicas = models.BooleanField(default=True)
    sanguineas = models.BooleanField(default=True)
    alergia = models.CharField(max_length=100, null=True, blank=True)
    activo = models.BooleanField(default=True)



    