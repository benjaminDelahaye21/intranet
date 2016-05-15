# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cra', '0002_auto_20160515_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commercial',
            name='liste_clients',
        ),
        migrations.AddField(
            model_name='commercial',
            name='liste_clients',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cra.Client'),
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='liste_consultants',
        ),
        migrations.AddField(
            model_name='commercial',
            name='liste_consultants',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cra.Consultant'),
        ),
    ]