# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gantt', '0003_activity_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityLinkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependency', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='activitylink',
            name='link_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gantt.ActivityLinkType'),
        ),
        migrations.AddField(
            model_name='activitylink',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='gantt.Activity'),
        ),
        migrations.AddField(
            model_name='activitylink',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='gantt.Activity'),
        ),
    ]