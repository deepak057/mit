# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaves',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='leaves',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users'),
        ),
    ]
