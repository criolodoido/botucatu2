# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-24 23:27
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queromais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipos', models.CharField(choices=[('CARD', 'Cardápio'), ('NOVID', 'Novidades'), ('CUPONS', 'Cupons'), ('INI', 'Inicial')], max_length=6)),
                ('titulo', models.CharField(max_length=100)),
                ('apresentacao', models.TextField()),
                ('imagem', cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem')),
                ('validade', models.DateField(null=True)),
                ('datapublicacao', models.DateField()),
            ],
        ),
    ]
