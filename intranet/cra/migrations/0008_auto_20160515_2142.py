# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 21:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cra', '0007_auto_20160515_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commercial2',
            name='liste_clients',
        ),
        migrations.RemoveField(
            model_name='commercial2',
            name='liste_consultants',
        ),
    ]
