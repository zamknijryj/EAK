# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170820_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='post/%Y/%m/%d'),
        ),
    ]
