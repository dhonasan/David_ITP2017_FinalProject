# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 05:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0019_auto_20171104_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
    ]