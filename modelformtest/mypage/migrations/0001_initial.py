# coding:utf-8
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
