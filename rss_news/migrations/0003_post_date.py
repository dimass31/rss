# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-19 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_news', '0002_auto_20171119_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default='2017-11-20'),
        ),
    ]
