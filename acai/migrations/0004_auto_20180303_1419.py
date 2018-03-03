# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-03 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acai', '0003_auto_20180226_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acai',
            name='datapublicacao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='acai',
            name='tipos',
            field=models.CharField(choices=[('CUPOM', 'Cupons'), ('CARD', 'Cardápio')], max_length=6),
        ),
        migrations.AlterField(
            model_name='acai',
            name='validade',
            field=models.DateField(),
        ),
    ]
