# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0003_auto_20160730_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo',
            name='slug',
            field=models.SlugField(default=123),
            preserve_default=False,
        ),
    ]