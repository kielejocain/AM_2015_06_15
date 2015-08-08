# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0007_auto_20150804_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofiles',
            name='user_logo',
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to=b'/images/', blank=True),
        ),
    ]
