# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gantt', '0002_auto_20160209_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='progress',
            field=models.FloatField(default=0.0),
        ),
    ]
