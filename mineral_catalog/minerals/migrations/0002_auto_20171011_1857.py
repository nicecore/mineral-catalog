# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='refractive_index',
            field=models.CharField(default='', max_length=255),
        ),
    ]
