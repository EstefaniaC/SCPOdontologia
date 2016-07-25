# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0007_paciente_ocupacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('receta', models.TextField(max_length=250, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('paciente', models.ForeignKey(blank=True, to='paciente.Paciente', null=True)),
            ],
        ),
    ]
