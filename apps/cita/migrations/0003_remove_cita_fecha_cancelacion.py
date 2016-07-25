# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0002_auto_20160522_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='fecha_cancelacion',
        ),
    ]
