# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-13 11:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_auto_20180911_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(max_length=254, upload_to='media')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='emp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webapp.Employee'),
        ),
    ]
