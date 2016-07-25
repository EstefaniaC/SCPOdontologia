# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tratamiento', '0001_initial'),
        ('paciente', '0003_paciente_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='celular',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='correo_electronico',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='observaciones',
            field=models.TextField(max_length=260, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='recomendado',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='tratamiento',
            field=models.ForeignKey(blank=True, to='tratamiento.Tratamiento', null=True),
        ),
    ]
