# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 23:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='Snippet',
        ),
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ('created',)},
        ),
    ]
