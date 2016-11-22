# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='cedula',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
