# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0007_paciente_ocupacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='motivo_consulta',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ocupacion',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='restauracion_protesica',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sangrado_encia',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
