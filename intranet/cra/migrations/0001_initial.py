# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('date_embauche', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
