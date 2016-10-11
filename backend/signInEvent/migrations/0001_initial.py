# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 15:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SignInEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name=b'Holding time')),
                ('type', models.IntegerField()),
                ('groupID', models.CharField(default=b'', max_length=255)),
                ('participant', models.ManyToManyField(related_name='participant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
