# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shublog', '0003_auto_20170911_1057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Article'},
        ),
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(verbose_name='create_date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(default='anonymous', editable=False, max_length=128, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_original',
            field=models.BooleanField(default=False, verbose_name='is_original'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_publish',
            field=models.BooleanField(default=True, verbose_name='is_publish'),
        ),
        migrations.AlterField(
            model_name='article',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modify_date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]