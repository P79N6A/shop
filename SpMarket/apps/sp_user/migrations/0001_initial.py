# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-20 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('nickname', models.CharField(blank=True, max_length=20, null=True, verbose_name='昵称')),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='手机号码')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], default=3, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生日期')),
                ('school_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='学校名称')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='学校详细地址')),
                ('hometown', models.CharField(blank=True, max_length=100, null=True, verbose_name='老家')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'db_table': 'sp_users',
            },
        ),
    ]
