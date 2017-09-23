# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 16:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpaceMap', '0005_city'),
        ('Character', '0003_auto_20170914_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='credits',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='ship',
            name='city_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SpaceMap.City'),
        ),
        migrations.AddField(
            model_name='ship',
            name='planate_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SpaceMap.Planet'),
        ),
        migrations.AddField(
            model_name='ship',
            name='system_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SpaceMap.StarSystem'),
        ),
        migrations.AlterField(
            model_name='character',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ship',
            name='character_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Character.Character'),
        ),
    ]
