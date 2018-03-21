# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-01 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180301_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='Slug will be generated automatically from the title of the post', unique=True),
        ),
    ]