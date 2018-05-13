# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-21 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180421_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scene',
            name='s',
        ),
        migrations.AddField(
            model_name='scene',
            name='scene_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]