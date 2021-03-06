# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 19:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank='True', upload_to='profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
