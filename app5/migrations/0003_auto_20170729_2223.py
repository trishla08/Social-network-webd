# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0002_userprofileinfo_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='status',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
