from django.db import models

from apps.tratamiento.models import Tratamiento

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30, null=True, blank=True)
    apellido_materno = models.CharField(max_length=30, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    lugar_nacimiento = models.CharField(max_length=30, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField(null=True, blank=True)
    celular = models.IntegerField(null=True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=160, null=True, blank=True)
    activo = models.BooleanField(default=True)
    recomendado = models.CharField(max_length=100, null=True, blank=True)
    observaciones = models.TextField(max_length=160, null=True, blank=True)
    motivo_consulta = models.CharField(max_length=50, null=True, blank=True)
    dolor = models.CharField(max_length=50, null=True, blank=True)
    control = models.CharField(max_length=50, null=True, blank=True)
    sangrado_encia = models.CharField(max_length=50, null=True, blank=True)
    restauracion_protesica = models.CharField(max_length=50, null=True, blank=True)
    enfermedad_actual = models.CharField(max_length=50, null=True, blank=True)
    tratamiento = models.ForeignKey(Tratamiento, null=True, blank=True)
    ocupacion = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return u'{} {} {}'.format(self.nombre, self.apellido_paterno, self.apellido_materno)