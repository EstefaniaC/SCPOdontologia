from django.db import models

from apps.paciente.models import Paciente
from apps.interconsulta.models import Interconsulta

# Create your models here.

class Consentimiento(models.Model):
    
    paciente = models.ForeignKey(Paciente)
    interconsulta = models.ForeignKey(Interconsulta)
    activo = models.BooleanField(default=True)
    