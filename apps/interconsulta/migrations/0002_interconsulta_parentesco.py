# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interconsulta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interconsulta',
            name='parentesco',
            field=models.TextField(max_length=50, null=True, blank=True),
        ),
    ]
