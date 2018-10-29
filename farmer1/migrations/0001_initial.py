# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('slug', models.SlugField()),
                ('text', models.TextField()),
                ('pic', models.ImageField(upload_to='home/')),
                ('pub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('slug', models.SlugField()),
                ('text', models.TextField()),
                ('pic', models.ImageField(upload_to='home/')),
                ('pub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='produce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('slug', models.SlugField()),
                ('text', models.TextField()),
                ('pic', models.ImageField(upload_to='home/')),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
