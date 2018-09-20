# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-20 18:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialglobo',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 20, 13, 42, 36, 678923)),
        ),
        migrations.AlterField(
            model_name='historialglobo',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 20, 13, 42, 36, 679041)),
        ),
        migrations.AlterField(
            model_name='historialglobo',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 20, 13, 42, 36, 678998)),
        ),
        migrations.AlterField(
            model_name='ocupacion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 20, 13, 42, 36, 674898)),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 20, 13, 42, 36, 673728)),
        ),
    ]