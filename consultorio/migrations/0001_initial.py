# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita_medica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_programada', models.DateField()),
                ('hora_programada', models.DateField()),
                ('fecha_atendida', models.DateField()),
                ('observacion', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('cedula', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('fecha_vinculacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cedula', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('passowrd', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='cita_medica',
            name='profesional',
            field=models.ForeignKey(blank=True, to='consultorio.Profesional', null=True),
        ),
        migrations.AddField(
            model_name='cita_medica',
            name='usuario',
            field=models.ForeignKey(blank=True, to='consultorio.Usuario', null=True),
        ),
    ]
