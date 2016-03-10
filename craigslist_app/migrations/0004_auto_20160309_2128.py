# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist_app', '0003_auto_20160309_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='craigslist_app.City'),
            preserve_default=False,
        ),
    ]
