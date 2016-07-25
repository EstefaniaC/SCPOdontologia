from django.db import models

from apps.paciente.models import Paciente

# Create your models here.


class Cita(models.Model):
    fecha = models.DateField()
    hora = models.CharField(max_length=7, null=True, blank=True)
    paciente = models.ForeignKey(Paciente)
    descripcion = models.TextField(max_length=260, null=True, blank=True)
    activo = models.BooleanField(default=True)
    estado = models.CharField(max_length=20, default="Agendada")