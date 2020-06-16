# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0010_auto_20150807_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
    ]
