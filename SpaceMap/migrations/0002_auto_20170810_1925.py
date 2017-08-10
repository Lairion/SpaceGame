# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpaceMap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starsystem',
            name='color',
            field=models.CharField(choices=[('#ff0000', 'Red'), ('#ffff66', 'Yellow'), ('#66ffff', 'Blue'), ('#ff66cc', 'Purpul'), ('#ccff99', 'Green')], max_length=8),
        ),
        migrations.AlterField(
            model_name='starsystem',
            name='mass',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='starsystem',
            name='size',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='starsystem',
            name='temp',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
