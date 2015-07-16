# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancematch_app', '0005_auto_20150716_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='danceprefs',
            name='activity',
            field=models.CharField(default=b'Active', max_length=200, choices=[(b'Active', b'Active'), (b'Casual', b'Casual'), (b'Inactive', b'Inactive')]),
        ),
    ]
