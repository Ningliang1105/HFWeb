# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-01 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=128)),
                ('number', models.DecimalField(decimal_places=1, max_digits=4)),
                ('publish_date', models.DateTimeField()),
                ('publish_edition', models.CharField(max_length=8)),
                ('post_time', models.DateTimeField(auto_now=True)),
                ('press', models.CharField(max_length=64)),
                ('translater', models.CharField(max_length=32)),
                ('book_author', models.CharField(max_length=32)),
                ('language', models.CharField(max_length=32)),
                ('mobile_number', models.DecimalField(decimal_places=1, max_digits=11)),
                ('email', models.EmailField(max_length=128)),
                ('address', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, to='Unibook.Tag'),
        ),
    ]
