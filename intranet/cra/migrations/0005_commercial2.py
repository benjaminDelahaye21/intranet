# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 20:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('cra', '0004_auto_20160515_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commercial2',
            fields=[
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('date_embauche', models.DateField(verbose_name="date d'embauche")),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('liste_clients', models.ManyToManyField(blank=True, null=True, to='cra.Client')),
                ('liste_consultants', models.ManyToManyField(blank=True, null=True, to='cra.Consultant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
