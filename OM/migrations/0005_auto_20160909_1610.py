# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-09 08:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OM', '0004_auto_20160909_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverlist',
            name='service_owner',
            field=models.ForeignKey(default='002', on_delete=django.db.models.deletion.CASCADE, to='OM.ServerGroup', verbose_name='\u670d\u52a1\u5668\u5c5e\u7ec4'),
        ),
    ]