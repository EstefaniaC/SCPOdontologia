# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tratamiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tratamiento',
            name='descripcion',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
