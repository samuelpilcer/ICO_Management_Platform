# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-14 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0002_auto_20180214_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='sale_state',
            field=models.CharField(default='not_started', max_length=100),
        ),
    ]
