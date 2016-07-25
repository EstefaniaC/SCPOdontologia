# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='cancelada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cita',
            name='fecha_cancelacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
