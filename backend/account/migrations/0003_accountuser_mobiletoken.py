# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20161011_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='mobileToken',
            field=models.CharField(default=b'', max_length=32),
        ),
    ]
