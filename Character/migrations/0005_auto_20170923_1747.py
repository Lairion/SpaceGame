# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Character', '0004_auto_20170919_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='evasion',
            field=models.IntegerField(default=0),
        ),
    ]