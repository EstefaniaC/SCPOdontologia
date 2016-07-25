# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antecedentesfamiliares', '0002_auto_20160721_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='artritis',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='cardiopatia',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='diabetes',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='epatitis',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='epilepsia',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='hipertension',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='malformacion',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='neoplasia',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='renales',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='sano',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='sida',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
