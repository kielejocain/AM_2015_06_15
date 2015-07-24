# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='name_text',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title_text',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
