# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_auto_20171116_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'permissions': (('customer_rights', 'Global customer rights'),),
            },
        ),
    ]
