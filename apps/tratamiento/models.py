from django.db import models

# Create your models here.

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.nombre)
