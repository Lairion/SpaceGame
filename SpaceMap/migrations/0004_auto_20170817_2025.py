# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 17:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SpaceMap', '0003_planet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planet',
            old_name='name',
            new_name='name_planet',
        ),
    ]
