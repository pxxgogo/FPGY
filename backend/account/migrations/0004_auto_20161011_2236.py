# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_accountuser_mobiletoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='personID',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
