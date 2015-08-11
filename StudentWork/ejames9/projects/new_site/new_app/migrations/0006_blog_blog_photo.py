# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0005_auto_20150730_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_photo',
            field=models.ImageField(null=True, upload_to=b'/static/new_app/images/', blank=True),
        ),
    ]
