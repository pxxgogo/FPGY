# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_activity_groupid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='groupID',
        ),
    ]