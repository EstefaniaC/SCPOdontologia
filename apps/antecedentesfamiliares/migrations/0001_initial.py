# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0007_paciente_ocupacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedentesFamiliares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diabetes', models.CharField(max_length=30, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
            ],
        ),
    ]
