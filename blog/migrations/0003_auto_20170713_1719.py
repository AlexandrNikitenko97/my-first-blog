# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_short_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='short_text',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
