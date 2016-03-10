# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist_app', '0004_auto_20160309_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craigslist_app.SubCategory')),
            ],
        ),
    ]