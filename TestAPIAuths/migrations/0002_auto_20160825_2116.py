# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestAPIAuths', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
