# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-10-21 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20181021_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Catagories'},
        ),
        migrations.RenameField(
            model_name='page',
            old_name='catagoty',
            new_name='category',
        ),
    ]
