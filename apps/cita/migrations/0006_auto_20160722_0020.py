# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0005_auto_20160715_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='hora',
            field=models.CharField(max_length=7, null=True, blank=True),
        ),
    ]
