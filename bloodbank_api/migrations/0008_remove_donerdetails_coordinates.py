# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-11 04:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank_api', '0007_donerdetails_coordinates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donerdetails',
            name='coordinates',
        ),
    ]
