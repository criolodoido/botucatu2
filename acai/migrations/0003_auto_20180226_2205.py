# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-26 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acai', '0002_auto_20180217_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acai',
            name='validade',
            field=models.DateTimeField(),
        ),
    ]