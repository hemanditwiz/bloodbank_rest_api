# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donerdetails',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]
