# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-15 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20180913_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(max_length=254, upload_to='media/%Y/%m/%d/'),
        ),
    ]
