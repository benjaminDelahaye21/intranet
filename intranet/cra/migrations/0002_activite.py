# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cra.Client')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cra.Consultant')),
            ],
        ),
    ]
