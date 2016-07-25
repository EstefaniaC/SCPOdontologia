from django.db import models

from apps.paciente.models import Paciente

# Create your models here.

class AntecedentesFamiliares(models.Model):

    paciente = models.ForeignKey(Paciente)
    diabetes = models.CharField(max_length=50, null=True, blank=True)
    hipertension = models.CharField(max_length=50, null=True, blank=True)
    cardiopatia = models.CharField(max_length=50, null=True, blank=True)
    neoplasia = models.CharField(max_length=50, null=True, blank=True)
    epilepsia = models.CharField(max_length=50, null=True, blank=True)
    malformacion = models.CharField(max_length=50, null=True, blank=True)
    sida = models.CharField(max_length=50, null=True, blank=True)
    renales = models.CharField(max_length=50, null=True, blank=True)
    epatitis = models.CharField(max_length=50, null=True, blank=True)
    artritis = models.CharField(max_length=50, null=True, blank=True)
    sano = models.CharField(max_length=50, null=True, blank=True)
    activo = models.BooleanField(default=True)
    