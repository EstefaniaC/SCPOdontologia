# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='receta',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
