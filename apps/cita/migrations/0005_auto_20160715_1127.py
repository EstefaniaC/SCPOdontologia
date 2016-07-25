# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0004_auto_20160523_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='cancelada',
        ),
        migrations.AddField(
            model_name='cita',
            name='estado',
            field=models.CharField(default=b'Agendada', max_length=20),
        ),
    ]
