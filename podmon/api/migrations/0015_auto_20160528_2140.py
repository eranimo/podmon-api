# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-28 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_account_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='key_id',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='v_code',
            field=models.CharField(max_length=65, unique=True),
        ),
    ]