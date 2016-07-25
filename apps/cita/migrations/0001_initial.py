# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_auto_20160521_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=5, null=True, blank=True)),
                ('descripcion', models.TextField(max_length=260)),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
            ],
        ),
    ]
