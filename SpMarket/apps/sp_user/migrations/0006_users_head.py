# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-23 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp_user', '0005_auto_20181120_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='head',
            field=models.ImageField(default='head/memtx.png', upload_to='head/%Y%m/', verbose_name='用户头像'),
        ),
    ]
