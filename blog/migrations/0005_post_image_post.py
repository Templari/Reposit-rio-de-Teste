# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171018_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_post',
            field=models.FileField(blank=True, upload_to='blog/uploads/postagem'),
        ),
    ]
