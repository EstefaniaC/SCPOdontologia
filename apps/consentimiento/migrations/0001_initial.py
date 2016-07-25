# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0009_auto_20160722_0020'),
        ('interconsulta', '0002_interconsulta_parentesco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consentimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activo', models.BooleanField(default=True)),
                ('interconsulta', models.ForeignKey(to='interconsulta.Interconsulta')),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
            ],
        ),
    ]
