# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Character', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='character_image/%Y/%m/%d'),
        ),
    ]
