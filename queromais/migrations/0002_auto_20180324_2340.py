# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-24 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queromais', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queromais',
            name='validade',
            field=models.DateField(blank=True, null=True),
        ),
    ]
