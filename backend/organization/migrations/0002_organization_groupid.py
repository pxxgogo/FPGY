# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='groupID',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
