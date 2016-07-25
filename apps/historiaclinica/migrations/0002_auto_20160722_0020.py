# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaclinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='ultima_consulta',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='ultima_radiografia',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
