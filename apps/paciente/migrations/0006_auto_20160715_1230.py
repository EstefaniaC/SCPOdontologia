# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_paciente_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='control',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='dolor',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='enfermedad_actual',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='lugar_nacimiento',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='motivo_consulta',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='restauracion_protesica',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sangrado_encia',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido_materno',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido_paterno',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='direccion',
            field=models.CharField(max_length=160, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(max_length=2),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='observaciones',
            field=models.TextField(max_length=160, null=True, blank=True),
        ),
    ]
