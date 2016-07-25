# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0006_auto_20160715_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='ocupacion',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
