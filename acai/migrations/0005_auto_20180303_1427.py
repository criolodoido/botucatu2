# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-03 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acai', '0004_auto_20180303_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acai',
            name='tipos',
            field=models.CharField(choices=[('CUPOM', 'Cupons'), ('CARD', 'Cardápio'), ('INI', 'Início')], max_length=6),
        ),
    ]
