# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0003_remove_cita_fecha_cancelacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='descripcion',
            field=models.TextField(max_length=260, null=True, blank=True),
        ),
    ]
