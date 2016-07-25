# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_auto_20160521_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='direccion',
            field=models.TextField(max_length=260, null=True, blank=True),
        ),
    ]
