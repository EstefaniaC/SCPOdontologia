# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tratamiento', '0002_auto_20160722_0020'),
        ('paciente', '0009_auto_20160722_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interconsulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('persona_responsable', models.CharField(max_length=100, null=True, blank=True)),
                ('diagnostico', models.TextField(max_length=500, null=True, blank=True)),
                ('complicaciones', models.TextField(max_length=500, null=True, blank=True)),
                ('motivo', models.TextField(max_length=500, null=True, blank=True)),
                ('servicio', models.TextField(max_length=500, null=True, blank=True)),
                ('resumen_clinico', models.TextField(max_length=500, null=True, blank=True)),
                ('estudio', models.TextField(max_length=500, null=True, blank=True)),
                ('criterio', models.TextField(max_length=500, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('paciente', models.ForeignKey(blank=True, to='paciente.Paciente', null=True)),
                ('tratamiento', models.ForeignKey(blank=True, to='tratamiento.Tratamiento', null=True)),
            ],
        ),
    ]
