# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist_app', '0009_auto_20160310_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='craigslist_app.City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='preferred_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='craigslist_app.City'),
        ),
    ]
