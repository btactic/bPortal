# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-03 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20180514_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortalSetting',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]
