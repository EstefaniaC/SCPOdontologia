# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0008_auto_20160722_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedentesPersonales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('varicela', models.BooleanField(default=True)),
                ('rubeola', models.BooleanField(default=True)),
                ('sarampion', models.BooleanField(default=True)),
                ('parotiditis', models.BooleanField(default=True)),
                ('tosferina', models.BooleanField(default=True)),
                ('escarlatina', models.BooleanField(default=True)),
                ('parasitosis', models.BooleanField(default=True)),
                ('hepatitis', models.BooleanField(default=True)),
                ('sida', models.BooleanField(default=True)),
                ('asma', models.BooleanField(default=True)),
                ('endocrina', models.BooleanField(default=True)),
                ('hipertension', models.BooleanField(default=True)),
                ('cancer', models.BooleanField(default=True)),
                ('enfermedad_sexual', models.BooleanField(default=True)),
                ('epilepsia', models.BooleanField(default=True)),
                ('amigdalitis', models.BooleanField(default=True)),
                ('tuberculosis', models.BooleanField(default=True)),
                ('reumatica', models.BooleanField(default=True)),
                ('diabetes', models.BooleanField(default=True)),
                ('cardiovasculares', models.BooleanField(default=True)),
                ('artritis', models.BooleanField(default=True)),
                ('traumatismo', models.BooleanField(default=True)),
                ('quirurgicas', models.BooleanField(default=True)),
                ('sanguineas', models.BooleanField(default=True)),
                ('alergia', models.CharField(max_length=100, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('paciente', models.ForeignKey(blank=True, to='paciente.Paciente', null=True)),
            ],
        ),
    ]
