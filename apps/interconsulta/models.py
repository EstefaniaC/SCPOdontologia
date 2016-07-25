from django.db import models

from apps.paciente.models import Paciente
from apps.tratamiento.models import Tratamiento
# Create your models here.

class Interconsulta(models.Model):
    
    paciente = models.ForeignKey(Paciente, null=True, blank=True)
    persona_responsable = models.CharField(max_length=100, null=True, blank=True)
    parentesco = models.TextField(max_length=50, null=True, blank=True)
    diagnostico = models.TextField(max_length=500, null=True, blank=True)
    complicaciones = models.TextField(max_length=500, null=True, blank=True)
    motivo = models.TextField(max_length=500, null=True, blank=True)
    servicio = models.TextField(max_length=500, null=True, blank=True)
    resumen_clinico = models.TextField(max_length=500, null=True, blank=True)
    estudio = models.TextField(max_length=500, null=True, blank=True)
    criterio= models.TextField(max_length=500, null=True, blank=True)
    tratamiento =models.ForeignKey(Tratamiento, null=True, blank=True)
    activo = models.BooleanField(default=True)
    