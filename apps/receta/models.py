from django.db import models

from apps.paciente.models import Paciente

# Create your models here.

class Receta(models.Model):
    
    paciente = models.ForeignKey(Paciente, null=True, blank=True)
    fecha = models.DateField()
    receta = models.TextField(max_length=500, null=True, blank=True)
    activo = models.BooleanField(default=True)